from graphviz import Source, Digraph


def draw_graph(connection_info):
    # 스크립트를 디버그하려면 하단 코드 줄의 중단점을 사용합니다.

    graph = Digraph()

    measures = {}
    for name, info in connection_info.items():
        status = 'green' if info['status'] else 'red'
        if name.endswith('measures'):
            measure = info['measure']
            graph.node(measure, shape='doublecircle', color=status)
            graph.node(name, shape='sqaure', color=status)
            graph.edge(measure, name)
            measures[name[:6]] = measure

        if info['measure'] == 'runway':
            measure = measures.get(name[7:13])
            graph.node(info['measure'], shape='doublecircle', color=status)
            graph.node(name, shape='sqaure', color=status)
            graph.edge(measure, info['measure'])
            graph.edge(info['measure'], name)

    return graph


graph = draw_graph(connection_info)

graph.view()
graph.render() # update
