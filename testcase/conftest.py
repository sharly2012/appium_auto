#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @author: sharly

import pytest


@pytest.fixture()
def action():
    print("null")


@pytest.fixture(scope="function")
def action_module():
    print("function")


@pytest.fixture(scope="class")
def action_module():
    print("class")


@pytest.fixture(scope="module")
def action_module():
    print("module")


@pytest.fixture(scope="session")
def action_module():
    print("session")
