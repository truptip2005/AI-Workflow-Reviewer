from reviewer.stage1_contracts import ApprovalRecord, ApprovalStatus
from reviewer.stage3_orchestrator import LocalFakeModelClient, WorkflowReviewer
from reviewer.stage4_eval import _base_valid_bundle, build_evaluation_dataset

def test_cache_invalidation_on_approval_change():
    """Regression 1: Changing an approval record must invalidate a cached PASS report."""
    bundle = _base_valid_bundle("REG_CACHE_01")
    reviewer = WorkflowReviewer(model_client=LocalFakeModelClient())

    rep1 = reviewer.review(bundle)
    assert rep1.status == "PASS"
    assert rep1.provenance["cache_hit"] is False

    rep2 = reviewer.review(bundle)
    assert rep2.provenance["cache_hit"] is True

    # Mutate approval: now requires 25 mins, while spec/workflow still implement 30 mins
    bundle.approvals.append(ApprovalRecord(
        approval_id="APR-NEW", target_req_id="R3", new_expression="wait_time >= 25 minutes",
        status=ApprovalStatus.APPROVED, revision=2, author="director"
    ))
    rep3 = reviewer.review(bundle)
    assert rep3.provenance["cache_hit"] is False
    assert rep3.status == "CHANGES_REQUIRED"

def test_hallucinated_llm_reference_stripped():
    """Regression 2: Model citing a non-existent rule ID must be filtered by guardrails."""
    bundle = _base_valid_bundle("REG_HALLUCINATION_02")
    reviewer = WorkflowReviewer(
        model_client=LocalFakeModelClient(fault_mode="hallucinated_ref"),
        enable_guardrails=True
    )
    rep = reviewer.review(bundle)
    assert rep.status == "PASS"
    assert all(f.rule_ref != "R99_INVENTED" for f in rep.findings)

def test_full_dataset_accuracy():
    dev, holdout = build_evaluation_dataset()
    for bundle, expected, fault in dev + holdout:
        reviewer = WorkflowReviewer(model_client=LocalFakeModelClient(fault_mode=None if fault == "none" else fault))
        assert reviewer.review(bundle).status == expected
