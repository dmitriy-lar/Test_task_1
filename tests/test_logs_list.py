import pytest

from ..main import logs_list


@pytest.mark.asyncio
async def test_logs_list_function():
    response = await logs_list(cont="hello_world_c", name="Log")
    assert b"Hello from Docker" in response[1][1]


@pytest.mark.asyncio
async def test_logs_list_functions_length():
    response = await logs_list(cont="hello_world_c", name="Log")
    assert 22 == len(response)
