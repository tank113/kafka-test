from src import myApp
from mock import patch
import pytest
import faust
from src.myApp import app

patch('myApp.topic-output', None)

def create_app():
    return faust.App('myApp')


@pytest.fixture()
def test_app(event_loop):
    app = create_app()
    app.finalize()
    app.flow_control.resume()
    return app

@pytest.mark.asyncio()
@pytest.fixture()
def event_loop():
    yield app.loop

@pytest.mark.asyncio()
async def test_collect_msg(test_app):
    async with myApp.collect_msg.test_context() as agent:
        event = await agent.put('hey')
        assert agent.results[event.message.offset] == 'hey'