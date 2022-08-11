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

class DiscAmplifier(SoSDiscipline):
    '''
    Testing discipline
    Implements "sound amplifier"
    Intended for coupling with DiscDistortion
    '''

    # ontology information
    _ontology_data = {
        'label': 'sos_trades_core.sos_wrapping.test_discs.disc_amplifier',
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
        'wave1': {'type': 'array', 'visibility': 'Shared', 'namespace': 'ns_wave_processing' },
        'rate': {'type': 'float', 'default': 1.0}
    }
    DESC_OUT = {
        'wave2': {'type': 'array', 'visibility': 'Shared', 'namespace': 'ns_wave_processing'},
    }

    def run(self):
        ''' Run discipline '''
        wave_in = self.get_sosdisc_inputs('wave1')
        rate = self.get_sosdisc_inputs('rate')

        wave_out = [ ]

        for vin in wave_in:
            vout = vin * rate

            wave_out.append(vout)

        dict_out = { }
        dict_out['wave2'] = wave_out
        self.store_sos_outputs_values(dict_out)
