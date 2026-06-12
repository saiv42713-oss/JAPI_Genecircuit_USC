import numpy as np
from pattern_metrics_reference import describe_pattern
from classify_regime import classify_regime_and_return_fields
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
# Test on 4 known parameter sets
test_cases = [
    (5.0, 2.0,  "?"),   # blob — true IRREGULAR?
    (4.0, 2.0,  "?"),   # near boundary
    (6.0, 3.0,  "?"),   # near boundary  
    (7.0, 4.0,  "?"),   # near boundary
    (5.0, 3.0,  "?"),   # near boundary
]
# Run each case, print metrics, and save final A field for sanity check
for ba, bi, expected in test_cases:
    final_A, final_B = classify_regime_and_return_fields(ba, bi)
    metrics = describe_pattern(final_A, final_B)
    print(f"\nba={ba}, bi={bi} (expected {expected}):")
    for k, v in metrics.items():
        print(f"  {k}: {v}")
    # Visualize final A field for sanity check
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(final_A, cmap='viridis', origin='lower')
    ax.set_title(f"ba={ba}, bi={bi} ({expected})")
    plt.savefig(f"calibration_ba{int(ba)}_bi{int(bi)}.png", 
                dpi=100, bbox_inches='tight')
    plt.close()