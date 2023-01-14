#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.5 (21G72) Kernel: Darwin 21.6.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : jkirchoff
# Created Date: Tue Sep 26 19:10:53 2022 CDT
# Last ModDate: Tue Sep 27 17:50:01 2022 CDT
# =============================================================================
import functools  # Reduce - Required for ID3 Header Checks
import json
from pprint import pprint
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from mutagen.id3 import ID3NoHeaderError  # Required for catching errors when no ID3 tag exists on the file.
from mutagen.id3 import Encoding  # Required for SYLT SYNC'D Lyrics
from mutagen.id3 import TPE1 as _TPE1  # TPE1 [ Version: 2.00 ] # Artist Name     - Lead Performer(s)/Soloist(s)
from mutagen.id3 import TIT2 as _TIT2  # TIT2 [ Version: 2.00 ] # Song Title      - Title/Song Name/content description
from mutagen.id3 import TALB as _TALB  # TALB [ Version: 2.00 ] # Album Title     - Movie/Show title
from mutagen.id3 import TPE2 as _TPE2  # TPE2 [ Version: 2.00 ] # Album Artist    - Band/orchestra/accompaniment
from mutagen.id3 import APIC as _APIC  # APIC [ Version: 4.20 ] # Album Cover     - Attached (or linked) Picture. id3.add(_APIC(encoding=3, mime=u'image/jpeg', type=3, desc=u'Front Cover', data=self.get_cover(info)))  Example2# id3.add(_APIC(encoding=3, mime=u'image/jpg', type=3, desc=u'Cover', data=self.get_cover(info['album_pic_url'])))
from mutagen.id3 import TCON as _TCON  # TCON [ Version: 2.00 ] # Genre           - Content type
from mutagen.id3 import TRCK as _TRCK  # TRCK [ Version: 2.00 ] # Track Number    - Position in set
from mutagen.id3 import TPOS as _TPOS  # TPOS [ Version: 2.00 ] # Disk Number     - Part of a set
from mutagen.id3 import WOAF as _WOAF  # WOAF [ Version: 2.00 ] # Official audio file webpage
from mutagen.id3 import WCOM as _WCOM  # WCOM [ Version: 2.00 ] # Commercial information
from mutagen.id3 import WOAR as _WOAR  # WOAR [ Version: 2.00 ] # Official artist/performer webpage
from mutagen.id3 import WOAS as _WOAS  # WOAS [ Version: 2.00 ] # Official audio source webpage
from mutagen.id3 import WORS as _WORS  # WORS [ Version: 2.00 ] # Official internet radio station homepage
from mutagen.id3 import TSO2 as _TSO2  # TSO2 [ Version: 2.00 ] # iTunes Album Artist Sort
from mutagen.id3 import TCMP as _TCMP  # TCMP [ Version: 2.00 ] # iTunes Part Of Compilation Flag
from mutagen.id3 import GRP1 as _GRP1  # GRP1 [ Version: 2.00 ] # iTunes Grouping
from mutagen.id3 import MVIN as _MVIN  # MVIN [ Version: 2.00 ] # iTunes Movement Number/Count
from mutagen.id3 import MVNM as _MVNM  # MVNM [ Version: 2.00 ] # iTunes Movement Name
from mutagen.id3 import PCST as _PCST  # PCST [ Version: 2.00 ] # iTunes Podcast Flag
from mutagen.id3 import TCAT as _TCAT  # TCAT [ Version: 2.00 ] # iTunes Podcast Category
from mutagen.id3 import TDES as _TDES  # TDES [ Version: 2.00 ] # iTunes Podcast Description
from mutagen.id3 import TGID as _TGID  # TGID [ Version: 2.00 ] # iTunes Podcast Identifier
from mutagen.id3 import TSOC as _TSOC  # TSOC [ Version: 2.00 ] # iTunes Composer Sort
from mutagen.id3 import WFED as _WFED  # WFED [ Version: 2.00 ] # iTunes Podcast Feed

from mutagen.id3 import AENC as _AENC  # AENC [ Version: 4.20 ] # id3.AENC(owner='', preview_start=0, preview_length=0, data='')
from mutagen.id3 import ASPI as _ASPI  # ASPI [ Version: 2.00 ] # Audio seek point index. Attributes: S, L, N, b, and Fi. For the meaning of these, see the ID3v2.4 specification. Fi is a list of integers.
from mutagen.id3 import CHAP as _CHAP  # CHAP [ Version: 2.00 ] # Chapter propertyHashKey An internal key used to ensure frame uniqueness in a tag
from mutagen.id3 import COMM as _COMM  # COMM [ Version: 4.11 ] # Comments
from mutagen.id3 import COMR as _COMR  # COMR [ Version: 4.25 ] # Commercial frame
from mutagen.id3 import CTOC as _CTOC  # CTOC [ Version: 2.00 ] # Table of contents propertyHashKey An internal key used to ensure frame uniqueness in a tag
from mutagen.id3 import ENCR as _ENCR  # ENCR [ Version: 4.26 ] # Encryption method registration
from mutagen.id3 import EQU2 as _EQU2  # EQU2 [ Version: 2.00 ] # Equalisation (2).  Attributes: method - interpolation method (0 = band, 1 = linear) desc - identifying description adjustments - list of (frequency, vol_adjustment) pairs
from mutagen.id3 import ETCO as _ETCO  # ETCO [ Version: 4.06 ] # Event timing codes
from mutagen.id3 import GEOB as _GEOB  # GEOB [ Version: 4.16 ] # General encapsulated object
from mutagen.id3 import GRID as _GRID  # GRID [ Version: 4.27 ] # Group identification registration
from mutagen.id3 import IPLS as _IPLS  # IPLS [ Version: 4.04 ] # Involved people list
from mutagen.id3 import LINK as _LINK  # LINK [ Version: 4.21 ] # Linked information
from mutagen.id3 import MCDI as _MCDI  # MCDI [ Version: 4.05 ] # Music CD identifier
from mutagen.id3 import MLLT as _MLLT  # MLLT [ Version: 4.07 ] # MPEG location lookup table
from mutagen.id3 import OWNE as _OWNE  # OWNE [ Version: 4.24 ] # Ownership frame
from mutagen.id3 import PCNT as _PCNT  # PCNT [ Version: 4.17 ] # Play counter
from mutagen.id3 import POPM as _POPM  # POPM [ Version: 4.18 ] # Popularimeter
from mutagen.id3 import POSS as _POSS  # POSS [ Version: 4.22 ] # Position synchronization frame
from mutagen.id3 import PRIV as _PRIV  # PRIV [ Version: 4.28 ] # Private frame
from mutagen.id3 import RBUF as _RBUF  # RBUF [ Version: 4.19 ] # Recommended buffer size
from mutagen.id3 import RVA2 as _RVA2  # RVA2 [ Version: 2.00 ] # Relative volume adjustment (2)
from mutagen.id3 import RVAD as _RVAD  # RVAD [ Version: 4.12 ] # Relative volume adjustment
from mutagen.id3 import RVRB as _RVRB  # RVRB [ Version: 4.14 ] # Reverb
from mutagen.id3 import SEEK as _SEEK  # SEEK [ Version: 2.00 ] # Seek frame.
from mutagen.id3 import SIGN as _SIGN  # SIGN [ Version: 2.00 ] # Signature frame.
from mutagen.id3 import SYLT as _SYLT  # SYLT [ Version: 4.10 ] # Synchronized lyric/text
from mutagen.id3 import SYTC as _SYTC  # SYTC [ Version: 4.08 ] # Synchronized tempo codes
from mutagen.id3 import TBPM as _TBPM  # TBPM [ Version: 2.00 ] # BPM (beats per minute)
from mutagen.id3 import TCOM as _TCOM  # TCOM [ Version: 2.00 ] # Composer
from mutagen.id3 import TCOP as _TCOP  # TCOP [ Version: 2.00 ] # Copyright message
from mutagen.id3 import TDAT as _TDAT  # TDAT [ Version: 2.00 ] # Date
from mutagen.id3 import TDEN as _TDEN  # TDEN [ Version: 2.00 ] # Encoding Time
from mutagen.id3 import TDLY as _TDLY  # TDLY [ Version: 2.00 ] # Playlist delay
from mutagen.id3 import TDOR as _TDOR  # TDOR [ Version: 2.00 ] # Original Release Time
from mutagen.id3 import TDRC as _TDRC  # TDRC [ Version: 2.00 ] # Recording Time
from mutagen.id3 import TDRL as _TDRL  # TDRL [ Version: 2.00 ] # Release Time
from mutagen.id3 import TDTG as _TDTG  # TDTG [ Version: 2.00 ] # Tagging Time
from mutagen.id3 import TENC as _TENC  # TENC [ Version: 2.00 ] # Encoded by
from mutagen.id3 import TEXT as _TEXT  # TEXT [ Version: 2.00 ] # Lyricist/Text writer
from mutagen.id3 import TFLT as _TFLT  # TFLT [ Version: 2.00 ] # File type
from mutagen.id3 import TIME as _TIME  # TIME [ Version: 2.00 ] # Time
from mutagen.id3 import TIPL as _TIPL  # TIPL [ Version: 2.00 ] # Involved People List
from mutagen.id3 import TIT1 as _TIT1  # TIT1 [ Version: 2.00 ] # Content group description
from mutagen.id3 import TIT3 as _TIT3  # TIT3 [ Version: 2.00 ] # Subtitle/Description refinement
from mutagen.id3 import TKEY as _TKEY  # TKEY [ Version: 2.00 ] # Initial key
from mutagen.id3 import TKWD as _TKWD  # TKWD [ Version: 2.00 ] # iTunes Podcast Keywords
from mutagen.id3 import TLAN as _TLAN  # TLAN [ Version: 2.00 ] # Language(s)
from mutagen.id3 import TLEN as _TLEN  # TLEN [ Version: 2.00 ] # Length
from mutagen.id3 import TMCL as _TMCL  # TMCL [ Version: 2.00 ] # Musicians Credits List
from mutagen.id3 import TMED as _TMED  # TMED [ Version: 2.00 ] # Media type
from mutagen.id3 import TMOO as _TMOO  # TMOO [ Version: 2.00 ] # Mood
from mutagen.id3 import TOAL as _TOAL  # TOAL [ Version: 2.00 ] # Original album/movie/show title
from mutagen.id3 import TOFN as _TOFN  # TOFN [ Version: 2.00 ] # Original filename
from mutagen.id3 import TOLY as _TOLY  # TOLY [ Version: 2.00 ] # Original lyricist(s)/text writer(s)
from mutagen.id3 import TOPE as _TOPE  # TOPE [ Version: 2.00 ] # Original artist(s)/performer(s)
from mutagen.id3 import TORY as _TORY  # TORY [ Version: 2.00 ] # Original release year
from mutagen.id3 import TOWN as _TOWN  # TOWN [ Version: 2.00 ] # File owner/licensee
from mutagen.id3 import TPE3 as _TPE3  # TPE3 [ Version: 2.00 ] # Conductor/performer refinement
from mutagen.id3 import TPE4 as _TPE4  # TPE4 [ Version: 2.00 ] # Interpreted, remixed, or otherwise modified by
from mutagen.id3 import TPRO as _TPRO  # TPRO [ Version: 2.00 ] # Produced (P)
from mutagen.id3 import TPUB as _TPUB  # TPUB [ Version: 2.00 ] # Publisher
from mutagen.id3 import TRDA as _TRDA  # TRDA [ Version: 2.00 ] # Recording dates
from mutagen.id3 import TRSN as _TRSN  # TRSN [ Version: 2.00 ] # Internet radio station name
from mutagen.id3 import TRSO as _TRSO  # TRSO [ Version: 2.00 ] # Internet radio station owner
from mutagen.id3 import TSIZ as _TSIZ  # TSIZ [ Version: 2.00 ] # Size
from mutagen.id3 import TSOA as _TSOA  # TSOA [ Version: 2.00 ] # Album Sort Order key
from mutagen.id3 import TSOP as _TSOP  # TSOP [ Version: 2.00 ] # Perfomer Sort Order key
from mutagen.id3 import TSOT as _TSOT  # TSOT [ Version: 2.00 ] # Title Sort Order key
from mutagen.id3 import TSRC as _TSRC  # TSRC [ Version: 2.00 ] # ISRC (international standard recording code)
from mutagen.id3 import TSSE as _TSSE  # TSSE [ Version: 2.00 ] # Software/Hardware and settings used for encoding
from mutagen.id3 import TSST as _TSST  # TSST [ Version: 2.00 ] # Set Subtitle
from mutagen.id3 import TXXX as _TXXX  # TXXX [ Version: 2.00 ] # User defined text information frame
from mutagen.id3 import TYER as _TYER  # TYER [ Version: 2.00 ] # Year
from mutagen.id3 import UFID as _UFID  # UFID [ Version: 4.01 ] # Unique file identifier
from mutagen.id3 import USER as _USER  # USER [ Version: 4.23 ] # Terms of use
from mutagen.id3 import USLT as _USLT  # USLT [ Version: 4.09 ] # UnSychronized lyric/text transcription
from mutagen.id3 import WCOP as _WCOP  # WCOP [ Version: 2.00 ] # Copyright/Legal information
from mutagen.id3 import WPAY as _WPAY  # WPAY [ Version: 2.00 ] # Payment
from mutagen.id3 import WPUB as _WPUB  # WPUB [ Version: 2.00 ] # Publishers official webpage
from mutagen.id3 import WXXX as _WXXX  # WXXX [ Version: 2.00 ] # User defined URL link frame

from mutagen.id3 import BUF as _BUF    # BUF  [ Version: 1.01 ] #
from mutagen.id3 import CNT as _CNT    # CNT  [ Version: 1.01 ] #
from mutagen.id3 import COM as _COM    # COM  [ Version: 1.01 ] #
from mutagen.id3 import CRA as _CRA    # CRA  [ Version: 1.01 ] #
from mutagen.id3 import CRM as _CRM    # CRM  [ Version: 1.01 ] #
from mutagen.id3 import ETC as _ETC    # ETC  [ Version: 1.01 ] #
from mutagen.id3 import GEO as _GEO    # GEO  [ Version: 1.01 ] #
from mutagen.id3 import GP1 as _GP1    # GP1  [ Version: 1.01 ] #
from mutagen.id3 import ID3 as _ID3    # ID3  [ Version: 1.01 ] #
from mutagen.id3 import IPL as _IPL    # IPL  [ Version: 1.01 ] #
from mutagen.id3 import LNK as _LNK    # LNK  [ Version: 1.01 ] #
from mutagen.id3 import MCI as _MCI    # MCI  [ Version: 1.01 ] #
from mutagen.id3 import MLL as _MLL    # MLL  [ Version: 1.01 ] #
from mutagen.id3 import MVI as _MVI    # MVI  [ Version: 1.01 ] #
from mutagen.id3 import MVN as _MVN    # MVN  [ Version: 1.01 ] #
from mutagen.id3 import PIC as _PIC    # PIC  [ Version: 1.01 ] #
from mutagen.id3 import POP as _POP    # POP  [ Version: 1.01 ] #
from mutagen.id3 import REV as _REV    # REV  [ Version: 1.01 ] #
from mutagen.id3 import RVA as _RVA    # RVA  [ Version: 1.01 ] #
from mutagen.id3 import SLT as _SLT    # SLT  [ Version: 1.01 ] #
from mutagen.id3 import STC as _STC    # STC  [ Version: 1.01 ] #
from mutagen.id3 import TAL as _TAL    # TAL  [ Version: 1.01 ] #
from mutagen.id3 import TBP as _TBP    # TBP  [ Version: 1.01 ] #
from mutagen.id3 import TCM as _TCM    # TCM  [ Version: 1.01 ] #
from mutagen.id3 import TCO as _TCO    # TCO  [ Version: 1.01 ] #
from mutagen.id3 import TCP as _TCP    # TCP  [ Version: 1.01 ] #
from mutagen.id3 import TCR as _TCR    # TCR  [ Version: 1.01 ] #
from mutagen.id3 import TDA as _TDA    # TDA  [ Version: 1.01 ] #
from mutagen.id3 import TDY as _TDY    # TDY  [ Version: 1.01 ] #
from mutagen.id3 import TEN as _TEN    # TEN  [ Version: 1.01 ] #
from mutagen.id3 import TFT as _TFT    # TFT  [ Version: 1.01 ] #
from mutagen.id3 import TIM as _TIM    # TIM  [ Version: 1.01 ] #
from mutagen.id3 import TKE as _TKE    # TKE  [ Version: 1.01 ] #
from mutagen.id3 import TLA as _TLA    # TLA  [ Version: 1.01 ] #
from mutagen.id3 import TLE as _TLE    # TLE  [ Version: 1.01 ] #
from mutagen.id3 import TMT as _TMT    # TMT  [ Version: 1.01 ] #
from mutagen.id3 import TOA as _TOA    # TOA  [ Version: 1.01 ] #
from mutagen.id3 import TOF as _TOF    # TOF  [ Version: 1.01 ] #
from mutagen.id3 import TOL as _TOL    # TOL  [ Version: 1.01 ] #
from mutagen.id3 import TOR as _TOR    # TOR  [ Version: 1.01 ] #
from mutagen.id3 import TOT as _TOT    # TOT  [ Version: 1.01 ] #
from mutagen.id3 import TP1 as _TP1    # TP1  [ Version: 1.01 ] #
from mutagen.id3 import TP2 as _TP2    # TP2  [ Version: 1.01 ] #
from mutagen.id3 import TP3 as _TP3    # TP3  [ Version: 1.01 ] #
from mutagen.id3 import TP4 as _TP4    # TP4  [ Version: 1.01 ] #
from mutagen.id3 import TPA as _TPA    # TPA  [ Version: 1.01 ] #
from mutagen.id3 import TPB as _TPB    # TPB  [ Version: 1.01 ] #
from mutagen.id3 import TRC as _TRC    # TRC  [ Version: 1.01 ] #
from mutagen.id3 import TRD as _TRD    # TRD  [ Version: 1.01 ] #
from mutagen.id3 import TRK as _TRK    # TRK  [ Version: 1.01 ] #
from mutagen.id3 import TS2 as _TS2    # TS2  [ Version: 1.01 ] #
from mutagen.id3 import TSA as _TSA    # TSA  [ Version: 1.01 ] #
from mutagen.id3 import TSC as _TSC    # TSC  [ Version: 1.01 ] #
from mutagen.id3 import TSI as _TSI    # TSI  [ Version: 1.01 ] #
from mutagen.id3 import TSP as _TSP    # TSP  [ Version: 1.01 ] #
from mutagen.id3 import TSS as _TSS    # TSS  [ Version: 1.01 ] #
from mutagen.id3 import TST as _TST    # TST  [ Version: 1.01 ] #
from mutagen.id3 import TT1 as _TT1    # TT1  [ Version: 1.01 ] #
from mutagen.id3 import TT2 as _TT2    # TT2  [ Version: 1.01 ] #
from mutagen.id3 import TT3 as _TT3    # TT3  [ Version: 1.01 ] #
from mutagen.id3 import TXT as _TXT    # TXT  [ Version: 1.01 ] #
from mutagen.id3 import TXX as _TXX    # TXX  [ Version: 1.01 ] #
from mutagen.id3 import TYE as _TYE    # TYE  [ Version: 1.01 ] #
from mutagen.id3 import UFI as _UFI    # UFI  [ Version: 1.01 ] #
from mutagen.id3 import ULT as _ULT    # ULT  [ Version: 1.01 ] #
from mutagen.id3 import WAF as _WAF    # WAF  [ Version: 1.01 ] #
from mutagen.id3 import WAR as _WAR    # WAR  [ Version: 1.01 ] #
from mutagen.id3 import WAS as _WAS    # WAS  [ Version: 1.01 ] #
from mutagen.id3 import WCM as _WCM    # WCM  [ Version: 1.01 ] #
from mutagen.id3 import WCP as _WCP    # WCP  [ Version: 1.01 ] #
from mutagen.id3 import WPB as _WPB    # WPB  [ Version: 1.01 ] #
from mutagen.id3 import WXX as _WXX    # WXX  [ Version: 1.01 ] #


class MP3TagYourSong(object):
    """
        Input:          self
        Output:         None
        Description:    MP3TagYourSong Handle Getters & Setters for Mutagen ID3 Tags
    """
    def __init__(self, arg: str):
        super(MP3TagYourSong, self).__init__()

        self.SONGpath = arg  # Full File Path To MP3.
        self.MP3HNDLR       = self.SetMP3Handle()
        self.ID3HNDLR       = ''
        self.ID3HNDLR       = self.SetID3Handle()

        self.SONGTITLENAME  = ''
        self.SONGTITLENAME  = self.getSongName()
        self.SONGARTISTNAME = ''
        self.SONGARTISTNAME = self.getSongArtist()

        self.SONGALBUMCOVER = ''
        self.SONGALBUMCOVER = self.getSongAlbumCover()
        self.SONGALBUMNAME  = ''
        self.SONGALBUMNAME  = self.getSongAlbum()
        self.SONGGENRE      = ''
        self.SONGGENRE      = self.getSongGenre()
        self.SONGTRACK      = ''
        self.SONGTRACK      = self.getSongTrack()

        self.SONGPLAYCOUNT  = 0
        self.SONGPLAYCOUNT  = self.getSongPlayCount()

        self.SONGSYNCLYRCS  = ''
        self.SONGSYNCLYRCS  = self.getSongSyncedLyrics()

        self.SONGPLAINLYRCS = ''
        self.SONGPLAINLYRCS = self.getSongUnSyncedLyrics()

        self.SONGDURATION   = 0
        self.SONGDURATION   = self.getSongInfoDuration()

    # =====================================================================================================================
    # Tag Checkers
    # =====================================================================================================================
    def CreateMissingTag(self):
        """
        Input:          self
        Output:         None
        Description:    To prevent an MP3 from throwing an error without tags, this will initialize tags on your song
                        Credit: https://github.com/quodlibet/mutagen/issues/327#issuecomment-339316014
        """
        try:
            mp3 = MP3(self.SONGpath)
            if mp3.tags is None:
                print(f"No ID3 Header or Tags Exist.")
                mp3.add_tags()
                print(f"Default Placeholder Tags Were Created.")
            tags = mp3.tags
            mp3.save()
        except Exception as e:
            print(f"{e}")

    def CheckID3Tag(self):
        """
        Input:  self
        Output: To prevent an MP3 from throwing an error without tags, this will initialize tags on your song

        Check for Header Size.
        """
        try:
            # print header data
            with open(self.SONGpath, 'rb') as a:
                data = a.read(10)
                # print(data)
            # print header data check
            with open(self.SONGpath, 'rb') as a:
                if data[0:3] != b'ID3':
                    print('No ID3 header present in file.')
                else:
                    size_encoded = bytearray(data[-4:])
                    size = functools.reduce(lambda a, b: (a * 128 + b), size_encoded, 0)
                    # print(size)
        except Exception as e:
            print(f"Error: {e}")

    def convertID3Tags2to3(self):
        """
        Update The ID3 Tags In The Files.
        """
        try:
            self.ID3HNDLR.update_to_v24()
            self.ID3HNDLR.save(v1=2, v2_version=4, v23_sep='/')
        except Exception as e:
            print(f"Error: {e}")

    def duration_from_seconds(self, s):
        """
        Module to get the convert Seconds to a time like format.
        """
        s = s
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        TIMELAPSED  = f"{d:03.0f}:{h:02.0f}:{m:02.0f}:{s:02.0f}"
        return TIMELAPSED

    def duration_from_millseconds(ms):
        """
        Module to get the convert Seconds to a time like format.
        """
        ms = ms
        s, ms = divmod(ms, 1000)
        m, s = divmod(s, 60)
        h, m = divmod(m, 60)
        d, h = divmod(h, 24)
        timelapsed = "{:01d}:{:02d}:{:02d}:{:02d}:{:02d}".format(int(d),
                                                                 int(h),
                                                                 int(m),
                                                                 int(s),
                                                                 int(ms))
        return timelapsed

    def deleteAllTags(self):
        """
        Input: self
        Output: Remove All ID3 Tags From A File Including The ID3 Header.
        """
        self.ID3HNDLR.delete(self.SONGpath)
        self.ID3HNDLR.save()
        return

    # =====================================================================================================================
    # Tag Getters
    # =====================================================================================================================
    def getOneSongToEdit(self):
        """
        JayRizzo Music Song Meta Mixer.
        """
        self.SONGpath = askopenfilename(initialdir=f"{self.CWDIR}/Music/",
                                        title="Choose A Song:",
                                        filetypes=[("MP3", "*.mp3"),
                                                   ("AAC Audio Files", "*.aac"),
                                                   ("AIFF Audio Files", "*.aiff"),
                                                   ("MPEG Audio Files", "*.mpeg"),
                                                   ("Protected Audio Files", "*.m4a"),
                                                   ("all", "*.*")])
        return self.SONGpath

    def getSongName(self):
        """
        Show Song Song Name/Title.
        """
        try:
            self.SONGTITLENAME = f"{self.ID3HNDLR.getall('TIT2')[0][0]}"
        except IndexError as e:
            self.SONGTITLENAME = ''
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SONGTITLENAME = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SONGTITLENAME

    def getSongArtist(self):
        """
        Show Song Artist Name.
        """
        try:
            self.SONGARTISTNAME = f"{self.ID3HNDLR.getall('TPE1')[0][0]}"
        except IndexError as e:
            self.SONGARTISTNAME
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SONGARTISTNAME = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SONGARTISTNAME

    def getSongAlbumArtist(self):
        """
        Show Song Album Name.
        """
        try:
            self.SONGALBUMARTIST = f"{self.ID3HNDLR.getall('TPE2')[0][0]}"
        except IndexError as e:
            self.SONGALBUMARTIST = ''
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SONGALBUMARTIST = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SONGALBUMARTIST

    def getSongAlbum(self):
        """
        Show Song Album Name.
        """
        try:
            self.SONGALBUMNAME = f"{self.ID3HNDLR.getall('TALB')[0][0]}"
        except IndexError as e:
            self.SONGALBUMNAME = ''
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SONGALBUMNAME = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SONGALBUMNAME

    def getSongPlayCount(self):
        """
        Show Song Play Count.
        """
        try:
            self.SONGPLAYCOUNT = f"{self.ID3HNDLR.getall('PCNT')[0].count}"
        except IndexError as e:
            self.SONGPLAYCOUNT = 0
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SONGPLAYCOUNT = 0
        except Exception as e:
            print(f"Error: {e}")
        return self.SONGPLAYCOUNT

    def getSongYear(self):
        """
        Show Song Play Count.
        """
        try:
            self.SONGYear = f"{self.ID3HNDLR.getall('TYER')[0][0]}"
        except IndexError as e:
            self.SONGYear = 0
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SONGYear = 0
        except Exception as e:
            print(f"Error: {e}")
        return self.SONGYear

    def getSongSyncedLyrics(self):
        """
        Show Synced Lyrics.
        """
        try:
            self.SONGSYNCLYRCS = self.ID3HNDLR.getall('SYLT::eng')
        except IndexError as e:
            self.SONGSYNCLYRCS = ''
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SONGSYNCLYRCS = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SONGSYNCLYRCS

    def getSongUnSyncedLyrics(self):
        """
        Show UnSynced Lyrics.
        """
        try:
            self.SONGPLAINLYRCS = self.ID3HNDLR.getall('USLT')
            print(f"{self.ID3HNDLR.get('USLT')}")
        except IndexError as e:
            self.SONGPLAINLYRCS = ''
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SONGPLAINLYRCS = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SONGPLAINLYRCS

    def getSongBPM(self):
        """
            Input: filename, BPM (int)
            Example: setSongUnSyncedLyrics('song', 'Some Lyics add Some More Lyics, add as many as you'd like')
        """
        try:
            self.SONGBPM = f"{self.ID3HNDLR.getall('TBPM')[0][0]}"
        except IndexError as e:
            self.SONGBPM = 0
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SONGBPM = 0
        except Exception as e:
            print(f"Error: {e}")
        return self.SONGBPM

    def getSongGenre(self):
        """
            Input: filename, BPM (int)
            Example: setSongUnSyncedLyrics('song', 'Some Lyics add Some More Lyics, add as many as you'd like')
        """
        try:
            self.SONGGENRE = f"{self.ID3HNDLR.getall('TCON')[0][0]}"
        except IndexError as e:
            self.SONGGENRE = ''
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SONGGENRE = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SONGGENRE


    def getSongTrack(self):
        """
            Input: filename, BPM (int)
            Example: setSongUnSyncedLyrics('song', 'Some Lyics add Some More Lyics, add as many as you'd like')
        """
        try:
            self.SONGTRACK = f"{self.ID3HNDLR.getall('TRCK')[0][0]}"
        except IndexError as e:
            self.SONGTRACK = ''
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SONGTRACK = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SONGTRACK


    def getSongAlbumCover(self):
        """
        Show Song Song Name/Title.
        """
        try:
            self.SONGALBUMCOVER = f"{self.ID3HNDLR.getall('APIC')[0]}"
        except IndexError as e:
            self.SONGALBUMCOVER = ''
        except ID3NoHeaderError as e:
            self.CreateMissingTag()
            self.SONGALBUMCOVER = ''
        except Exception as e:
            print(f"Error: {e}")
        return self.SONGALBUMCOVER

    # =====================================================================================================================
    # MP3 Tag Getters
    # =====================================================================================================================
    def getSongInfoAlbumGain(self):
        if self.MP3HNDLR.info.album_gain is None:
            self.MP3HNDLR.info.album_gain = 0
        else:
            self.MP3HNDLR.info.album_gain
        return self.MP3HNDLR.info.album_gain

    def getSongInfoAlbumPeak(self):
        if self.MP3HNDLR.info.album_peak is None:
            self.MP3HNDLR.info.album_peak = 0
        else:
            self.MP3HNDLR.info.album_peak
        return self.MP3HNDLR.info.album_peak

    def getSongInfoBitrate(self):
        x = int(self.MP3HNDLR.info.bitrate/1000)
        y = f"{x} kbps"
        return (x, y)

    def getSongInfoBitrateMode(self):
        return self.MP3HNDLR.info.bitrate_mode

    def getSongInfoChannels(self):
        return self.MP3HNDLR.info.channels

    def getSongInfoEncoderInfo(self):
        return self.MP3HNDLR.info.encoder_info

    def getSongInfoEncoderSettings(self):
        return self.MP3HNDLR.info.encoder_settings

    def getSongInfoFrameOffset(self):
        return self.MP3HNDLR.info.frame_offset

    def getSongInfoLayer(self):
        return self.MP3HNDLR.info.layer

    def getSongInfoDuration(self):
        self.SetID3Handle()
        return self.MP3HNDLR.info.length

    def getSongInfoMode(self):
        # One of STEREO, JOINTSTEREO, DUALCHANNEL, or MONO (0-3)")
        if self.MP3HNDLR.info.mode == 0:
            x = 'STEREO'
        elif self.MP3HNDLR.info.mode == 1:
            x = 'JOINTSTEREO'
        elif self.MP3HNDLR.info.mode == 2:
            x = 'DUALCHANNEL'
        elif self.MP3HNDLR.info.mode == 3:
            x = 'MONO'
        else:
            x = ''
        return x

    def getSongInfoPadding(self):
        return self.MP3HNDLR.info.padding

    def getSongInfoProtected(self):
        return self.MP3HNDLR.info.protected

    def getSongInfoSketchy(self):
        return self.MP3HNDLR.info.sketchy

    def getSongInfoSampleRate(self):
        x = self.MP3HNDLR.info.sample_rate
        y = f"{x} kHz"
        return (x, y)

    def getSongInfoTrackGain(self):
        if self.MP3HNDLR.info.track_gain is None:
            self.MP3HNDLR.info.track_gain = 0
        else:
            self.MP3HNDLR.info.track_gain
        return self.MP3HNDLR.info.track_gain

    def getSongInfoTrackPeak(self):
        if self.MP3HNDLR.info.track_peak is None:
            self.MP3HNDLR.info.track_peak = 0
        else:
            self.MP3HNDLR.info.track_peak
        return self.MP3HNDLR.info.track_peak

    def getSongInfoVersion(self):
        # print(f"Song Inf Version: {self.MP3HNDLR.info.version}")
        return self.MP3HNDLR.info.version

    def getSongTagVersion(self):
        # print(f"Song tags Version: {self.MP3HNDLR.tags.version}")
        # print(f"Song Tag Version: {dir(self.MP3HNDLR.tags)}")
        return self.MP3HNDLR.tags.version

    def getSongTagSize(self):
        return self.MP3HNDLR.tags.size

    def getSongTagKeyPairs(self):
        return self.MP3HNDLR.tags.items()

    def getSongUnknownTags(self):
        # print(f"Unknown Keys: {dir(self.MP3HNDLR.tags)}")
        return self.MP3HNDLR.tags.unknown_frames

    def getAvailibleTagDescriptions(self):
        print(f"\nList of All Availible Items In This Song {self.SONGpath}\n")
        for i in sorted(self.MP3HNDLR.keys()):
            match i:
                case 'APIC:':       print(f"\t{i} -- Album Cover Image")
                case 'COMM::eng':  print(f"\t{i} -- English Comment")
                case 'COMM:ID3v1 Comment:eng':  print(f"\t{i} -- ID3v1 English Comment")
                case 'ETCO':       print(f"\t{i} -- Event timing codes")
                case 'GEOB':       print(f"\t{i} -- General encapsulated object")
                case 'GRID':       print(f"\t{i} -- Group identification registration")
                case 'GRP1':       print(f"\t{i} -- iTunes Grouping")
                case 'IPLS':       print(f"\t{i} -- Involved people list")
                case 'LINK':       print(f"\t{i} -- Linked information")
                case 'MCDI':       print(f"\t{i} -- Music CD identifier")
                case 'MLLT':       print(f"\t{i} -- MPEG location lookup table")
                case 'MVIN':       print(f"\t{i} -- iTunes Movement Number/Count")
                case 'MVNM':       print(f"\t{i} -- iTunes Movement Name")
                case 'OWNE':       print(f"\t{i} -- Ownership frame")
                case 'PCNT':       print(f"\t{i} -- Play counter")
                case 'PCST':       print(f"\t{i} -- iTunes Podcast Flag")
                case 'POPM':       print(f"\t{i} -- Popularimeter")
                case 'POSS':       print(f"\t{i} -- Position synchronization frame")
                case 'PRIV':       print(f"\t{i} -- Private frame")
                case 'RBUF':       print(f"\t{i} -- Recommended buffer size")
                case 'RVA2':       print(f"\t{i} -- Relative volume adjustment (2)")
                case 'RVAD':       print(f"\t{i} -- Relative volume adjustment")
                case 'RVRB':       print(f"\t{i} -- Reverb")
                case 'SEEK':       print(f"\t{i} -- Seek frame.")
                case 'SIGN':       print(f"\t{i} -- Signature frame.")
                case 'SYLT':       print(f"\t{i} -- Synchronized lyric/text")
                case 'SYTC':       print(f"\t{i} -- Synchronized tempo codes")
                case 'TALB':       print(f"\t{i} -- Album")
                case 'TBPM':       print(f"\t{i} -- BPM (beats per minute)")
                case 'TCAT':       print(f"\t{i} -- iTunes Podcast Category")
                case 'TCMP':       print(f"\t{i} -- Part Of Compilation Flag")
                case 'TCOM':       print(f"\t{i} -- Composer")
                case 'TCON':       print(f"\t{i} -- Genre")
                case 'TCOP':       print(f"\t{i} -- Copyright message")
                case 'TDAT':       print(f"\t{i} -- Date")
                case 'TDEN':       print(f"\t{i} -- Encoding Time")
                case 'TDES':       print(f"\t{i} -- iTunes Podcast Description")
                case 'TDLY':       print(f"\t{i} -- Playlist delay")
                case 'TDOR':       print(f"\t{i} -- Original Release Time")
                case 'TDRC':       print(f"\t{i} -- Recording Time")
                case 'TDRC':       print(f"\t{i} -- Year")
                case 'TDRL':       print(f"\t{i} -- Release Time")
                case 'TDTG':       print(f"\t{i} -- Tagging Time")
                case 'TENC':       print(f"\t{i} -- Encoded by")
                case 'TEXT':       print(f"\t{i} -- Lyricist/Text writer")
                case 'TFLT':       print(f"\t{i} -- File type")
                case 'TGID':       print(f"\t{i} -- iTunes Podcast Identifier")
                case 'TIME':       print(f"\t{i} -- Time")
                case 'TIPL':       print(f"\t{i} -- Involved People List")
                case 'TIT1':       print(f"\t{i} -- Content group description")
                case 'TIT2':       print(f"\t{i} -- Song Name")
                case 'TIT3':       print(f"\t{i} -- Subtitle/Description refinement")
                case 'TKEY':       print(f"\t{i} -- Initial key")
                case 'TKWD':       print(f"\t{i} -- iTunes Podcast Keywords")
                case 'TLAN':       print(f"\t{i} -- Language(s)")
                case 'TLEN':       print(f"\t{i} -- Length")
                case 'TMCL':       print(f"\t{i} -- Musicians Credits List")
                case 'TMED':       print(f"\t{i} -- Media type")
                case 'TMOO':       print(f"\t{i} -- Mood")
                case 'TOAL':       print(f"\t{i} -- Original album/movie/show title")
                case 'TOFN':       print(f"\t{i} -- Original filename")
                case 'TOLY':       print(f"\t{i} -- Original lyricist(s)/text writer(s)")
                case 'TOPE':       print(f"\t{i} -- Original artist(s)/performer(s)")
                case 'TORY':       print(f"\t{i} -- Original release year")
                case 'TOWN':       print(f"\t{i} -- File owner/licensee")
                case 'TPE1':       print(f"\t{i} -- Artist")
                case 'TPE2':       print(f"\t{i} -- Album artist")
                case 'TPE3':       print(f"\t{i} -- Conductor/performer refinement")
                case 'TPE4':       print(f"\t{i} -- Interpreted, remixed, or otherwise modified by")
                case 'TPOS':       print(f"\t{i} -- Disk Number")
                case 'TPRO':       print(f"\t{i} -- Produced (P)")
                case 'TPUB':       print(f"\t{i} -- Publisher")
                case 'TRCK':       print(f"\t{i} -- Track")
                case 'TRDA':       print(f"\t{i} -- Recording dates")
                case 'TRSN':       print(f"\t{i} -- Internet radio station name")
                case 'TRSO':       print(f"\t{i} -- Internet radio station owner")
                case 'TSIZ':       print(f"\t{i} -- Size")
                case 'TSO2':       print(f"\t{i} -- iTunes Album Artist Sort")
                case 'TSOA':       print(f"\t{i} -- Album Sort Order key")
                case 'TSOC':       print(f"\t{i} -- iTunes Composer Sort")
                case 'TSOP':       print(f"\t{i} -- Perfomer Sort Order key")
                case 'TSOT':       print(f"\t{i} -- Title Sort Order key")
                case 'TSRC':       print(f"\t{i} -- ISRC (international standard recording code)")
                case 'TSSE':       print(f"\t{i} -- Software/Hardware and settings used for encoding")
                case 'TSST':       print(f"\t{i} -- Set Subtitle")
                case 'TXXX':       print(f"\t{i} -- User defined text information frame")
                case 'TYER':       print(f"\t{i} -- Year")
                case 'UFID':       print(f"\t{i} -- Unique file identifier")
                case 'USER':       print(f"\t{i} -- Terms of use")
                case 'USLT':       print(f"\t{i} -- UnSychronized lyric/text transcription")
                case 'WCOM':       print(f"\t{i} -- Commercial information")
                case 'WCOP':       print(f"\t{i} -- Copyright/Legal information")
                case 'WFED':       print(f"\t{i} -- iTunes Podcast Feed")
                case 'WOAF':       print(f"\t{i} -- Official audio file webpage")
                case 'WOAR':       print(f"\t{i} -- Official artist/performer webpage")
                case 'WOAS':       print(f"\t{i} -- Official audio source webpage")
                case 'WORS':       print(f"\t{i} -- Official internet radio station homepage")
                case 'WPAY':       print(f"\t{i} -- Payment")
                case 'WPUB':       print(f"\t{i} -- Publishers official webpage")
                case 'WXXX':       print(f"\t{i} -- User defined URL link frame")
                case _:
                    print(f"UnMapped: {i}")
        return


    # =====================================================================================================================
    # Tag Setters
    # =====================================================================================================================

    def SetMP3Handle(self):
        """
            Input: (None)
            Example: SetMP3Handle(self)
        """
        self.MP3HNDLR = MP3(self.SONGpath)
        return self.MP3HNDLR

    def SetID3Handle(self):
        """
            Input: (None)
            Example: SetID3Handle(self)
        """
        self.ID3HNDLR = ID3(self.SONGpath)
        return self.ID3HNDLR

    def setSongArtist(self, ArtistName: str):
        """
            Input: filename, ArtistName (STRING)
            Example: setSongArtist('song', 'Artist Name')
        """
        self.SONGARTISTNAME = ArtistName
        self.ID3HNDLR.add(_TPE1(encoding=3, text=[ArtistName]))
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')

    def setSongAlbumArtist(self, AlbumArtist: str):
        """
            Input: filename, AlbumName (STRING)
            Example: setSongAlbumArtist('song', 'Album Name')
        """
        self.SONGALBUMARTIST = AlbumArtist
        self.ID3HNDLR.add(_TPE2(encoding=3, text=[AlbumArtist]))
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')

    def setSongAlbum(self, AlbumName: str):
        """
            Input: filename, AlbumName (STRING)
            Example: setSongAlbum('song', 'Album Name')
        """
        self.SONGALBUMNAME = AlbumName
        self.ID3HNDLR.add(_TALB(encoding=3, text=[AlbumName]))
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')

    def setSongTitle(self, SongTitle: str):
        """
            Input: filename, SongTitle (STRING)
            Example: setSongTitle('song', 'Song Title')
        """
        self.ID3HNDLR.add(_TIT2(encoding=3, text=[SongTitle]))
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')

    def setSongPlayCount(self, PlayCount: str):
        """
            Input: filename, PlayCount (str)
            Example: setSongPlayCount('song', 1531]
        """
        PlayCount = int(PlayCount)
        self.ID3HNDLR.add(_PCNT(encoding=3, count=PlayCount))
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')

    def setSongSyncedLyrics(self, sync_lyrics : list):
        """
            Input: filename, sync_lyrics  list((TupledPairs, 1042), (TupledPairs, 2042), (TupledPairs, 3042))
            # self.SYNC_LYRICS = [('', 0), ('', 0)]

            Example: setSongSyncedLyrics('song', [('Some Lyics at time in MilliSeconds', 1000), ('Some More Lyics, add as many as you'd like, 2000)]
        """
        slrcs = sync_lyrics
        self.ID3HNDLR.setall("SYLT", [SYLT(encoding=3, lang='eng', format=2, type=1, text=slrcs)])
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')

    def setSongUnSyncedLyrics(self, lyrics : str):
        """
            Input: filename, sync_lyrics (String)
            Example: setSongUnSyncedLyrics('song', 'Some Lyics add Some More Lyics, add as many as you'd like')
        """
        slrcs = lyrics
        self.ID3HNDLR.setall("USLT", [USLT(encoding=3, lang='eng', format=2, type=1, text=slrcs)])
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')

    def setSongBPM(self, bpm : int):
        """
            Input: filename, BPM (int)
            Example: setSongUnSyncedLyrics('song', 'Some Lyics add Some More Lyics, add as many as you'd like')
        """
        sBPM = bpm
        self.ID3HNDLR.add(_TBPM(encoding=3, speed=sBPM))
        # self.ID3HNDLR.setall("TBPM", [TBPM(encoding=3, lang='eng', format=2, type=1, bpm=sBPM)])
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')


    def setSongGenre(self, SongGenre : str):
        """
            Input: filename, SongGenre : str
            Example: setSongUnSyncedLyrics('song', 'Some Lyics add Some More Lyics, add as many as you'd like')
        """
        self.ID3HNDLR.add(_TCON(encoding=3, text=[SongGenre]))
        self.ID3HNDLR.save(v1=1, v2_version=4, v23_sep='/')


    def setSongAlbumCover(self, cover_path : str):
        """
            Input: filename, cover_path : str
            Example:  add album cover
        """
        self.ID3HNDLR.add(_APIC(
            # encoding=3
              encoding=3
            , mime='image/jpeg'
            , type=3  #  3 is for the cover(front) image
            , desc=u'Cover'
            , data=open(cover_path, 'rb').read()
            )   )




# "TSO2": "albumartistsort", # iTunes extension
# "TSOC": "composersort", # iTunes extension
# "TCMP": "compilation", # iTunes extension
# "TCOM": "composer",
# "TCOP": "copyright",
# "TENC": "encodedby",
# "TEXT": "lyricist",
# "TLEN": "length",
# "TMED": "media",
# "TMOO": "mood",
# "TIT3": "version",
# "TPE2": "performer",
# "TPE3": "conductor",
# "TPE4": "arranger",     remixer = TextField(ID3.TPE4)
# "TPOS": "discnumber",   disc = SizeField(ID3.TPOS)
# "TPUB": "organization", publisher = TextField(ID3.TPUB)
# "TRCK": "tracknumber",  track = SizeField(ID3.TRCK)
# "TOLY": "author",
# "TSOA": "albumsort",
# "TSOP": "artistsort",
# "TSOT": "titlesort",
# "TSRC": "isrc",
# "TSST": "discsubtitle",

# TIT1
# TIT2
# TIT3
#     release = TextField(ID3.COMM)

#     key = TextField(ID3.TKEY)
#     year = TextField(ID3.TDRC)
#     genre = TextField(ID3.TCON)


if __name__ == '__main__':
    # =====================================================================================================================
    # Example Song
    # =====================================================================================================================
    # filename = '/Users/jayrizzo/Documents/git/MP3Player/Music/Cowabunga (Original Mix).mp3'
    filename = "/Users/jayrizzo/Music/Music/Media.localized/Music/Compilations/Now That's What I Call Music! 77/1-21 In My System.mp3"

    # ID3HNDLR = ID3(filename)
    # pprint(dict(ID3HNDLR), indent=4, width=1)
    song = MP3TagYourSong(filename)
    # song.deleteAllTags()  # TUrning this on will clear all headers and you must recreate them manually.  THERE IS NO UNDO!!!!

            # encoding=3,  # UTF-8
    # Checkers
    song.CreateMissingTag()
    song.CheckID3Tag()
    song.convertID3Tags2to3()

    # Getters
    print("\n# {0} File MetaData Details {0}".format('=' * 25))
    print(f"Song Title Name                 {song.getSongName()}")
    print(f"Song Artist Name:               {song.getSongArtist()}")
    print(f"Song Album Name:                {song.getSongAlbum()}")
    print(f"Song Album Cover:               {len(song.getSongAlbumCover())} bytes")
    print(f"Song Play Count:                {song.getSongPlayCount()}")
    print(f"Song BPM:                       {song.getSongBPM()}")
    print(f"Song Genre:                     {song.getSongGenre()}")

    print("\n# {0} MP3 File INFO Details {0}".format('=' * 25))
    print(f"Song Total Duration(t):         {song.duration_from_seconds(song.getSongInfoDuration())}")
    print(f"Song Total Duration(s):         {song.getSongInfoDuration()}")
    print(f"Song Info AlbumGain:            {song.getSongInfoAlbumGain()}")
    print(f"Song Info AlbumPeak:            {song.getSongInfoAlbumPeak()}")
    print(f"Song Info Bitrate:              {song.getSongInfoBitrate()}")
    print(f"Song Info BitrateMode:          {song.getSongInfoBitrateMode()}")
    print(f"Song Info Channels:             {song.getSongInfoChannels()}")
    print(f"Song Info EncoderInfo:          {song.getSongInfoEncoderInfo()}")
    print(f"Song Info EncoderSettings:      {song.getSongInfoEncoderSettings()}")
    print(f"Song Info FrameOffset:          {song.getSongInfoFrameOffset()}")
    print(f"Song Info Layer:                {song.getSongInfoLayer()}")
    print(f"Song Info Mode:                 {song.getSongInfoMode()}")
    print(f"Song Info Padding:              {song.getSongInfoPadding()}")
    print(f"Song Info Protected:            {song.getSongInfoProtected()}")
    print(f"Song Info Sketchy:              {song.getSongInfoSketchy()}")
    print(f"Song Info SampleRate:           {song.getSongInfoSampleRate()}")
    print(f"Song Info TrackGain:            {song.getSongInfoTrackGain()}")
    print(f"Song Info TrackPeak:            {song.getSongInfoTrackPeak()}")
    print(f"Song Info Version:              {song.getSongInfoVersion()}")

    print("\n# {0} MP3 File TAG Details {0}".format('=' * 25))
    print(f"Song Tag Version:               {song.getSongTagVersion()}")
    print(f"Song Tag Size:                  {song.getSongTagSize()}")
    # print(f"Song Tag Keys:                  {pprint(dict(song.getSongTagKeyPairs()), indent=4, width=1)}")
    print(f"Song UnknownTags:               {song.getSongUnknownTags()}")
    print(f"Song UnknownTags:               {song.getAvailibleTagDescriptions()}")
    print()
