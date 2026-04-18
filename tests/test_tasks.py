import importlib
import pytest


# -----------------------------
# Student list (normalized)
# -----------------------------
STUDENTS = [
    "52518", "52653", "52494", "52698", "52672", "54342", "52501", "52559",
    "52671", "52793", "52637", "52607", "49830", "52697", "52626", "52568",
    "52578", "52552", "52482", "52703", "49991", "54346", "52683", "52707",
    "52453", "52662", "52588", "52561", "52610", "47527", "52785", "52571",
    "52620", "52679", "48772", "52604", "53462", "52658", "52676", "52696",
    "52545", "52511", "52512", "52548", "52509", "51790", "52781", "52544",
    "52443", "52791", "52593", "52666", "52670", "52606", "52721", "52678",
    "52633", "52438", "49872", "47581", "52508", "52496", "52439",
    "48409-ex", "48419-ex", "48438-ex", "48436-ex", "52627",
]


# -----------------------------
# Utility
# -----------------------------
def digits_of(id_str: str):
    """Extract digits from ID (ignoring -ex)."""
    return [int(ch) for ch in id_str if ch.isdigit()]


# -----------------------------
# Reference implementations
# -----------------------------
def ref_52518(id): return sum(d for d in digits_of(id) if d % 2 == 0)
def ref_52653(id):
    p = 1
    for d in digits_of(id):
        if d != 0: p *= d
    return p
def ref_52494(id):
    ds = digits_of(id)
    return sum(ds[i] for i in range(len(ds)) if i % 2 == 1)
def ref_52698(id):
    ds = digits_of(id)
    return max(ds) - min(ds)
def ref_52672(id): return sum(1 for d in digits_of(id) if d > 5)
def ref_54342(id): return sum(d*d for d in digits_of(id))
def ref_52501(id): return sum(digits_of(id)) % 7
def ref_52559(id): return digits_of(id).count(5)
def ref_52671(id): return sum(digits_of(id)[:3])
def ref_52793(id):
    ds = digits_of(id)
    p = 1
    for d in ds[-3:]: p *= d
    return p
def ref_52637(id):
    primes = {2,3,5,7}
    return sum(d for d in digits_of(id) if d in primes)
def ref_52607(id):
    s = sum(digits_of(id))
    while s >= 10:
        s = sum(int(c) for c in str(s))
    return s
def ref_49830(id):
    ds = sorted(digits_of(id))
    return int("".join(str(d) for d in ds))
def ref_52697(id):
    ds = digits_of(id)
    return sum(ds[i] for i in range(len(ds)) if i % 2 == 0)
def ref_52626(id): return sum(1 for d in digits_of(id) if d % 2 == 0)
def ref_52568(id):
    ds = digits_of(id)
    p = 1
    for i in range(0, len(ds), 2): p *= ds[i]
    return p
def ref_52578(id): return sum(d for d in digits_of(id) if d % 3 == 0)
def ref_52552(id):
    ds = digits_of(id)
    se = sum(d for d in ds if d % 2 == 0)
    so = sum(d for d in ds if d % 2 == 1)
    return abs(se - so)
def ref_52482(id): return max(digits_of(id))
def ref_52703(id):
    ds = [d for d in digits_of(id) if d != 0]
    return min(ds)
def ref_49991(id): return digits_of(id).count(9)
def ref_54346(id): return sum(set(digits_of(id)))
def ref_52683(id):
    ds = digits_of(id)
    p = 1
    for i in range(1, len(ds), 2): p *= ds[i]
    return p
def ref_52707(id): return sum(d for d in digits_of(id) if d != 0)
def ref_52453(id):
    ds = digits_of(id)
    return sum(ds[:2]) - sum(ds[-2:])
def ref_52662(id):
    ds = digits_of(id)
    return sum(1 for d in set(ds) if ds.count(d) > 1)
def ref_52588(id): return sum(d*d for d in digits_of(id))
def ref_52561(id): return ref_52607(id)
def ref_52610(id): return ref_52653(id)
def ref_47527(id): return sum(d for d in digits_of(id) if d <= 4)
def ref_52785(id):
    ds = digits_of(id)
    return sum(d for d in ds if ds.count(d) == 1)
def ref_52571(id): return sum(1 for d in digits_of(id) if d >= 7)
def ref_52620(id):
    ds = digits_of(id)
    return sum(ds) - max(ds)
def ref_52679(id): return ref_52653(id)
def ref_48772(id): return sum(sorted(digits_of(id)))
def ref_52604(id): return sum(d for d in digits_of(id) if d % 2 == 0 or d % 3 == 0)
def ref_53462(id): return ref_52552(id)
def ref_52658(id):
    ds = digits_of(id)
    return sum(ds[i] for i in [1,3,4] if i < len(ds))
def ref_52676(id): return digits_of(id).count(6)
def ref_52696(id):
    ds = digits_of(id)
    return sum(ds) - min(ds)
def ref_52545(id): return ref_52637(id)
def ref_52511(id): return digits_of(id).count(1)
def ref_52512(id):
    ds = digits_of(id)
    idx = [0,2,4]
    p = 1
    for i in idx:
        if i < len(ds): p *= ds[i]
    return p
def ref_52548(id): return sum(d for d in digits_of(id) if d > 4)
def ref_52509(id): return ref_52707(id)
def ref_51790(id): return ref_52653(id)
def ref_52781(id): return sum(d for d in digits_of(id) if d % 2 == 1)
def ref_52544(id): return digits_of(id).count(4)
def ref_52443(id):
    ds = digits_of(id)
    return sum(d for d in ds if ds.count(d) == 1)
def ref_52791(id): return sum(digits_of(id))
def ref_52593(id):
    ds = [d for d in digits_of(id) if d >= 3]
    p = 1
    for d in ds: p *= d
    return p
def ref_52666(id): return sum(digits_of(id))
def ref_52670(id): return sum(1 for d in digits_of(id) if d % 5 == 0)
def ref_52606(id): return ref_52707(id)
def ref_52721(id):
    ds = digits_of(id)
    return sum(ds[i] for i in range(2, min(5, len(ds))))
def ref_52678(id):
    ds = [d for d in digits_of(id) if d % 2 == 0]
    p = 1
    for d in ds: p *= d
    return p
def ref_52633(id):
    ds = digits_of(id)
    return sum(d for d in set(ds) if ds.count(d) > 1)
def ref_52438(id): return ref_52698(id)
def ref_49872(id): return sum(d for d in digits_of(id) if d < 7)
def ref_47581(id):
    primes = {2,3,5,7}
    ds = [d for d in digits_of(id) if d in primes]
    p = 1
    for d in ds: p *= d
    return p
def ref_52508(id): return ref_52707(id)
def ref_52496(id):
    ds = digits_of(id)
    return sum(ds[i] for i in range(1, min(4, len(ds))))
def ref_52439(id): return sum(1 for d in digits_of(id) if d in (3,9))
def ref_48409_ex(id): return sum(digits_of(id))
def ref_48419_ex(id): return ref_52653(id)
def ref_48438_ex(id): return ref_52518(id)
def ref_48436_ex(id): return ref_52552(id)
def ref_52627(id): return sum(d for d in digits_of(id) if d >= 6)


# -----------------------------
# Mapping ID → reference function
# -----------------------------
REF_MAP = {
    "52518": ref_52518, "52653": ref_52653, "52494": ref_52494,
    "52698": ref_52698, "52672": ref_52672, "54342": ref_54342,
    "52501": ref_52501, "52559": ref_52559, "52671": ref_52671,
    "52793": ref_52793, "52637": ref_52637, "52607": ref_52607,
    "49830": ref_49830, "52697": ref_52697, "52626": ref_52626,
    "52568": ref_52568, "52578": ref_52578, "52552": ref_52552,
    "52482": ref_52482, "52703": ref_52703, "49991": ref_49991,
    "54346": ref_54346, "52683": ref_52683, "52707": ref_52707,
    "52453": ref_52453, "52662": ref_52662, "52588": ref_52588,
    "52561": ref_52561, "52610": ref_52610, "47527": ref_47527,
    "52785": ref_52785, "52571": ref_52571, "52620": ref_52620,
    "52679": ref_52679, "48772": ref_48772, "52604": ref_52604,
    "53462": ref_53462, "52658": ref_52658, "52676": ref_52676,
    "52696": ref_52696, "52545": ref_52545, "52511": ref_52511,
    "52512": ref_52512, "52548": ref_52548, "52509": ref_52509,
    "51790": ref_51790, "52781": ref_52781, "52544": ref_52544,
    "52443": ref_52443, "52791": ref_52791, "52593": ref_52593,
    "52666": ref_52666, "52670": ref_52670, "52606": ref_52606,
    "52721": ref_52721, "52678": ref_52678, "52633": ref_52633,
    "52438": ref_52438, "49872": ref_49872, "47581": ref_47581,
    "52508": ref_52508, "52496": ref_52496, "52439": ref_52439,
    "48409-ex": ref_48409_ex, "48419-ex": ref_48419_ex,
    "48438-ex": ref_48438_ex, "48436-ex": ref_48436_ex,
    "52627": ref_52627,
}


# -----------------------------
# Module name resolver
# -----------------------------
def module_name_for(id_str: str) -> str:
    safe = id_str.replace("-", "_")
    return f"solutions.task_{safe}"


# -----------------------------
# Parametrized test
# -----------------------------
@pytest.mark.parametrize("student_id", STUDENTS)
def test_student_task(student_id):
    mod = importlib.import_module(module_name_for(student_id))
    solve = getattr(mod, "solve")
    expected = REF_MAP[student_id](student_id)
    result = solve(student_id)
    assert isinstance(result, int)
    assert result == expected
