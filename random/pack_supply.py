def pack_supplies(supply_count: int, crate_capacity: int, pack_capacity: int) -> tuple[int, int, int]:
    full_crates: int = supply_count // crate_capacity
    
    count_left_after_crates: int = supply_count % crate_capacity
    packs_capacity: int = count_left_after_crates // pack_capacity
    
    count_left_after_packs: int = count_left_after_crates % pack_capacity
    
    return (full_crates, packs_capacity, count_left_after_packs)

print(pack_supplies(137, 24, 5))
# (5, 3, 2)    
