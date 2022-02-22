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

__copyright__ = "Copyright (c) 2008-2021 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "Apache License, Version 2.0"
""" The license for the module """

import math

import appier

class Graph(object):
    """
    Graph structure and associated algorithms. Made up by a dictionary of
    sources to destinations and costs (weighted edges).
    Edges are unidirectional by default.
    Costs default to a unit.
    """

    def __init__(self):
        self.edges = dict()

    @classmethod
    def _build_path(cls, prev, src, dst):
        """
        Builds the shortest path given dictionary
        of previous nodes.
        """

        cur, path = dst, []
        while cur != src:
            path.append(cur)
            cur = prev[cur]
        path.append(src)
        path.reverse()
        return path

    def add_edges(self, edges):
        for edge in edges:
            if len(edge) < 2: continue
            src, dst = edge[0], edge[1]
            cost = edge[2] if len(edge) > 2 and isinstance(edge[2], int) else 1
            bidirectional = edge[3] if len(edge) > 3 and isinstance(edge[3], bool) else False
            self.add_edge(src, dst, cost = cost, bidirectional = bidirectional)

    def add_edge(self, src, dst, cost = 1, bidirectional = False):
        if src not in self.edges: self.edges[src] = []
        self.edges[src].append((dst, cost))

        if bidirectional: self.add_edge(dst, src, cost = cost, bidirectional = False)

    def dijkstra(self, src, dst):
        """
        Dijkstra's algorithm with priority queue implementation.
        """

        if src == dst: return [src], 0

        dist, prev = dict(), dict()
        dist[src] = 0

        queue = appier.MemoryQueue()
        queue.push(src, priority = 0)

        while queue.length() > 0:
            (_, _, top) = queue.pop(full = True)
            dist[top] = math.inf if top not in dist else dist[top]

            edges = self.edges[top] if top in self.edges else []
            for (nxt, cost) in edges:
                dist[nxt] = math.inf if nxt not in dist else dist[nxt]

                alt = dist[top] + cost
                if alt < dist[nxt]:
                    dist[nxt] = alt
                    prev[nxt] = top
                    queue.push(nxt, priority = dist[nxt])

        return self._build_path(prev, src, dst), dist[dst]
