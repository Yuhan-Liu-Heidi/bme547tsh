import pytest


@pytest.mark.parametrize("NameIn, NameOut", [
    (["Heidi Liu", "Sara Qi"],
        (["Heidi", "Sara"],
            ["Liu", "Qi"])),
    (["Heidi H Liu", "Sara Qi", "Chenx Yang"],
        (["Heidi", "Sara", "Chenx"],
            ["Liu", "Qi", "Yang"]))
    ])
@pytest.mark.parametrize("TSHIn, TSHOut", [
    (["TSH,1,0.5,2", "TSH,2,1,3", "TSH,1.2,2,2,4.1"],
        ([["0.5", "1", "2"],
            ["1", "2", "3"],
                ["1.2", "2", "2", "4.1"]],
                    ["Hypothyroidism", "Normal thyroid function", "Hyperthyroidism"]
        )
    )
    ])
def test_sort_name(NameIn, NameOut):
    from tsh import sort_name
    result = sort_name(NameIn)
    assert result == NameOut


def test_sort_tsh(TSHIn):
    from tsh import sort_tsh
    result = sort_tsh(TSHIn)
    assert result == TSHOut
