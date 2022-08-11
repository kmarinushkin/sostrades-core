'''
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''

from sos_trades_core.execution_engine.sos_discipline import SoSDiscipline
from sympy.series import limitseq

class DiscDistortion(SoSDiscipline):
    '''
    Testing discipline
    Implements guitar pedal effect "distortion" (clipping)
    '''

    # ontology information
    _ontology_data = {
        'label': 'sos_trades_core.sos_wrapping.test_discs.disc_distortion',
        'type': 'Fake',
        'source': 'SoSTrades Project',
        'validated': '',
        'validated_by': 'SoSTrades Project',
        'last_modification_date': '',
        'category': '',
        'definition': '',
        'icon': '',
        'version': '',
    }

    _maturity = 'Fake'

    DESC_IN = {
        'wave': {'type': 'array' },
        'limit': {'type': 'float', 'default': 0.8}
    }
    DESC_OUT = {
        'wave1': {'type': 'array', 'visibility': 'Shared', 'namespace': 'ns_wave_processing'},
    }

    def run(self):
        ''' Run discipline '''
        wave_in = self.get_sosdisc_inputs('wave')
        limit = self.get_sosdisc_inputs('limit')

        wave_out = [ ]

        for vin in wave_in:
            vout = vin

            if (vin > 0) and (vin > limit):
                vout = limit
            elif (vin < 0) and (vin < -limit):
                vout = -limit

            wave_out.append(vout)

        dict_out = { }
        dict_out['wave1'] = wave_out
        self.store_sos_outputs_values(dict_out)
