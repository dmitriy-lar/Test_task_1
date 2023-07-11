import asyncio
import aiohttp


async def logs_list(cont, name):
    """This function returns a list of tuples of logs lines"""
    result = []
    conn = aiohttp.UnixConnector(path="/var/run/docker.sock")
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(
            f"http://xx/containers/{cont}/logs?follow=1&stdout=1"
        ) as resp:
            async for line in resp.content:
                result.append((name, line))
    return result


async def logs_response(cont):
    """This function returns a response of request"""
    conn = aiohttp.UnixConnector(path="/var/run/docker.sock")
    async with aiohttp.ClientSession(connector=conn) as session:
        async with session.get(
            f"http://xx/containers/{cont}/logs?follow=1&stdout=1"
        ) as resp:
            return resp
