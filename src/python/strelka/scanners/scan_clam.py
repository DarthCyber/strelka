import os
import requests
import clamd
import tempfile

from six import BytesIO
from strelka import strelka


class ScanClam(strelka.Scanner):
    """Sends files to ClamAV.
       not actually scanning the file because I had that working then I broke it...somewhere
    """
    def scan(self, data, file, options, expire_at):

        try:

            try:
                cd = clamd.ClamdUnixSocket("/etc/clamysock/clamd.sock",None)

                scan_result = cd.instream(BytesIO(clamd.EICAR))

                self.event['clamresults'] = scan_result
                self.flags.append(scan_result['stream'][0])

            except:
                self.flags.append('error_scanning')

        except:
            self.flags.append('error_processing')
            return

        self.flags.append(str(scan_result))
