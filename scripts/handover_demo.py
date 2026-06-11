from src.adaptive_handover import AdaptiveHandover, CandidateCell


def main():
    controller = AdaptiveHandover(min_reward_gap=0.1)

    candidates_t1 = [
        CandidateCell("BS-1", rsrp=0.8, los=0.9, delay=0.1, packet_loss=0.02, handover_required=False),
        CandidateCell("BS-2", rsrp=0.7, los=0.8, delay=0.2, packet_loss=0.04, handover_required=True),
    ]

    selected = controller.update_current_cell(candidates_t1)
    print(f"Initial cell: {selected}")

    candidates_t2 = [
        CandidateCell("BS-1", rsrp=0.5, los=0.4, delay=0.3, packet_loss=0.08, handover_required=False),
        CandidateCell("BS-2", rsrp=0.9, los=0.95, delay=0.08, packet_loss=0.01, handover_required=True),
    ]

    selected = controller.update_current_cell(candidates_t2)
    print(f"After evaluation: {selected}")


if __name__ == "__main__":
    main()
