import pytest

from ..main import logs_response


@pytest.mark.asyncio
async def test_logs_response_function():
    response = await logs_response(cont="hello_world_c")
    assert True == response.ok
    assert 200 == response.status


@pytest.mark.asyncio
async def test_logs_response_function_content_type():
    response = await logs_response(cont="hello_world_c")
    assert "application/vnd.docker.multiplexed-stream" == response.content_type
