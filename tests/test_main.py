# -*- mode: python -*- -*- coding: utf-8 -*-

def test_read_main(test_app):
    response = test_app.get('/users')
    assert response.status_code == 200
