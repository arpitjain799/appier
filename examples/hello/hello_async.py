#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Appier Framework
# Copyright (c) 2008-2022 Hive Solutions Lda.
#
# This file is part of Hive Appier Framework.
#
# Hive Appier Framework is free software: you can redistribute it and/or modify
# it under the terms of the Apache License as published by the Apache
# Foundation, either version 2.0 of the License, or (at your option) any
# later version.
#
# Hive Appier Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# Apache License for more details.
#
# You should have received a copy of the Apache License along with
# Hive Appier Framework. If not, see <http://www.apache.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2022 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import appier

class HelloApp(appier.App):

    def __init__(self, *args, **kwargs):
        appier.App.__init__(
            self,
            name = "hello",
            *args, **kwargs
        )

    @appier.route("/hello.tpl", "GET")
    async def hello_template_async(self):
        await appier.header_a()
        yield await self.template_async(
            "hello.txt",
            message = "hello world"
        )

    @appier.route("/hello_sync.tpl", "GET")
    def hello_template_sync(self):
        return self.template(
            "hello.txt",
            message = "hello world"
        )

    @appier.exception_handler(appier.NotFoundError)
    def not_found(self, error):
        return "Not found error"

    @appier.error_handler(404)
    def not_found_code(self, error):
        return "404 - Not found"

app = HelloApp()
app.serve()
