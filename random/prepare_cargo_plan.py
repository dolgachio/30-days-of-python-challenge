from typing import Optional


def prepare_cargo_plan(
    manifests: dict[str, tuple[str, int | None]],
    fallback_weights: dict[str, int] | None,
) -> dict[str, list[tuple[str, int]]]:
    prepared = {}

    for destination in manifests:
        prepared_entries = []
        
        for item_name, weight in manifests[destination]:
            final_weight = weight
            if (
                final_weight is None
                and fallback_weights is not None
                and item_name in fallback_weights
            ):
                final_weight = fallback_weights[item_name]
            
            prepared_entries.append((item_name, final_weight))
        prepared[destination] = prepared_entries

    return prepared
