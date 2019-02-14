import pytest


""""@pytest.mark.parametrize("NameIn, NameOut", [
    (["Heidi Liu", "Sara Qi"],
        (["Heidi", "Sara"],
            ["Liu", "Qi"])),
    (["Heidi H Liu", "Sara Qi", "Chenx Yang"],
        (["Heidi", "Sara", "Chenx"],
            ["Liu", "Qi", "Yang"]))
    ])
def test_sort_name(NameIn, NameOut):
    from tsh import sort_name
    result = sort_name(NameIn)
    assert result == NameOut
"""


@pytest.mark.parametrize("tshin, tshout", [
    (["TSH,1.1,1.2,1.5", "TSH,3.5,4,4.1"],
        ["Normal thyroid function", "Hyperthyroidism"]),
    (["TSH,0.8,1,2"], ["Hypothyroidism"])
])
def test_sort_tsh(tshin, tshout):
    from tsh import sort_tsh
    result = sort_tsh(tshin)
    assert result[1] == tshout
