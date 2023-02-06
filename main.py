from graphviz import Source, Graph, Digraph
from datetime import datetime, tzinfo

connection_info = {'hsds-1-measures': {
    'measure': 'drill-01',
    'query': 'hsds-1-measures',
    'status': True,
    # 'last_seen': datetime(2023, 2, 3, 18, 12, 42, 935939, tzinfo='Asia/Seoul'),
    'last_date': '2 days,23 hours'},
    'runway-hsds-1-anomaly-score': {
        'measure': 'runway',
        'query': 'runway-hsds-1-anomaly-score',
        'status': False,
        # 'last_seen': datetime(2023, 2, 3, 9, 12, 42, 935000, tzinfo='UTC'),
        'last_date': '2 days,24 hours'},
    'runway-hsds-1-recon': {
        'measure': 'runway',
        'query': 'runway-hsds-1-recon',
        'status': False,
        # 'last_seen': datetime(2023, 2, 3, 9, 12, 42, 935000, tzinfo='UTC'),
        'last_date': '2 days,24 hours'},
    'runway-hsds-1-recon-error': {
        'measure': 'runway',
        'query': 'runway-hsds-1-recon-error',
        'status': False,
        # 'last_seen': datetime(2023, 2, 3, 9, 12, 42, 935000, tzinfo='UTC'),
        'last_date': '2 days,24 hours'}
}

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