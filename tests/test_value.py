import pytest
import jsonschema

from gemd_schema.value import (
    real_value,
    integer_value,
    categorical,
    composition,
    molecular_structure,
)


@pytest.mark.parametrize(
    "value",
    [
        {"type": "normal_real", "units": "kelvin", "mean": 350, "std": 1.03},
        {
            "type": "uniform_real",
            "units": "meter",
            "lower_bound": 0.9995,
            "upper_bound": 1.0005,
        },
        {"type": "nominal_real", "units": "meter", "nominal": 1.0},
    ],
)
def test_real_value(value):
    assert jsonschema.validate(value, real_value) is None


@pytest.mark.parametrize(
    "value",
    [
        {"type": "uniform_integer", "lower_bound": 245, "upper_bound": 254},
        {"type": "nominal_integer", "nominal": 42},
    ],
)
def test_integer_value(value):
    assert jsonschema.validate(value, integer_value) is None


@pytest.mark.parametrize(
    "value",
    [
        {"type": "discrete_categorical", "probabilities": {"red": 0.54, "blue": 0.46}},
        {"type": "nominal_categorical", "category": "red"},
    ],
)
def test_categorical(value):
    assert jsonschema.validate(value, categorical) is None


@pytest.mark.parametrize(
    "value",
    [
        {"type": "nominal_composition", "quantities": {"water": 120, "ethanol": 80}},
        {"type": "empirical_formula", "formula": "SiO2"},
    ],
)
def test_composition(value):
    assert jsonschema.validate(value, composition) is None


@pytest.mark.parametrize(
    "value",
    [
        {"type": "smiles", "smiles": "c1(C=O)cc(OC)c(O)cc1"},
        {
            "type": "inchi",
            "inchi": "InChI=1S/C6H6O3/c7-4-1-2-5(8)6(9)3-4/h1-3H,(H,7,8)(H,9,10)",
        },
    ],
)
def test_molecular_structure(value):
    assert jsonschema.validate(value, molecular_structure) is None
