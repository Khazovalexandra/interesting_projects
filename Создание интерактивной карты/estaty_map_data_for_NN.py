# '56.326797, 44.006516'
from estaty.analysis.action import Analyzer
from estaty.data_source.action import DataSource
from estaty.main import EstateModel
from estaty.preprocessing.action import Preprocessor

import warnings
warnings.filterwarnings('ignore')


def load_data_from_osm():
    
    osm_source = DataSource('osm', params={'category': 'park'})

    osm_reprojected = Preprocessor('reproject', params={'to': 'auto'}, from_actions=[osm_source])

    analysis = Analyzer('distance', params={'network_type': 'walk', 'visualize': True, 'color': '#C67E00',
                                            'edgecolor': 'black', 'title': 'Parks'},
                        from_actions=[osm_reprojected])

    model = EstateModel().for_property({'lat': 56.326797, 'lon': 44.0065167}, radius=5000)
    loaded_data = model.compose(analysis)

    print(loaded_data)

    print(loaded_data.lines)
    print(f'Min length: {loaded_data.lines["Length"].min():.2f}, m')
    print(f'Mean length: {loaded_data.lines["Length"].mean():.2f}, m')
    print(f'Max length: {loaded_data.lines["Length"].max():.2f}, m')

if __name__ == '__main__':
    load_data_from_osm()