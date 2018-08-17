# -*- coding: utf-8 -*-

"""
MIT License

Copyright (c) 2018 Samuel Riches

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import sanic

import logging
import helpers

bp = sanic.Blueprint('API-Routes')
log = logging.getLogger(__name__)


@bp.route("/ip/redirect", methods=["GET"])
async def ip_redirect_tracker(request):
    try:
        url = request.args["url"]
    except KeyError:
        try:
            url = request.json.get("url")
        except (AttributeError, KeyError):
            error = """Please specify one or more IP Addresses under the "ip" query parameter
                (multiple or space separated) or as a json body under the "ip" (single) or
                "addresses" (array) keys."""
            return sanic.response.json({"error": error}, status=400)

    if await helpers.url_validator(url):
        pass
    else:
        return sanic.response.json({"error": "URL is not in a valid format. Please try again."}, status=400)
