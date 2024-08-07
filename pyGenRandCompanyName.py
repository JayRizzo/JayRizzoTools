#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created Syst: macOS Monterey 12.4 (21F79) Kernel: Darwin 21.5.0
# Created Plat: Python 3.10.5 ('v3.10.5:f377153967', 'Jun  6 2022 12:36:10')
# Created By  : Jeromie Kirchoff
# Created Date: Mon Jun 13 03:22:59 2022 CDT
# Last ModDate: Sun Feb 18 19:45:00 2024 CDT
# =============================================================================
# Notes:
# =============================================================================

from random import choice

def rand_company_name():
    """Return a Random Company Name."""
    xo = [
          "3M Company"
        , "A-Mark Precious Metals"
        , "A.O. Smith"
        , "Abbott Laboratories"
        , "AbbVie Incorporated"
        , "AbbVie"
        , "Abercrombie & Fitch"
        , "ABM Industries"
        , "Academy Sports and Outdoors"
        , "Acadia Healthcare"
        , "Activision Blizzard"
        , "Acuity Brands"
        , "Acushnet Holdings"
        , "AdaptHealth"
        , "Adobe"
        , "ADT"
        , "Advance Auto Parts"
        , "Advanced Micro Devices"
        , "Advantage Solutions"
        , "AECOM"
        , "Aerojet Rocketdyne Holdings"
        , "AES"
        , "Affiliated Managers Group"
        , "Aflac"
        , "AGCO"
        , "Agilent Technologies"
        , "AIG"
        , "Air Products & Chemicals"
        , "Airbnb"
        , "Akamai Technologies"
        , "Alaska Air Group"
        , "Albemarle"
        , "Albertsons Cos., Incorporated"
        , "Albertsons"
        , "Alcoa"
        , "Alexandria Real Estate Equities"
        , "Alight"
        , "Align Technology"
        , "Alleghany"
        , "Alliant Energy"
        , "Allison Transmission Holdings"
        , "Allstate"
        , "Ally Financial"
        , "Alpha Metallurgical Resources"
        , "Alphabet Incorporated"
        , "Alphabet"
        , "Altaba Incorporated"
        , "Altice USA"
        , "Altria Group"
        , "Amazon"
        , "Amazon.com Incorporated"
        , "AMC Entertainment Holdings"
        , "AMC Networks"
        , "AMC Theaters"
        , "Amedisys"
        , "Amerco"
        , "Ameren"
        , "American Airlines Group Incorporated"
        , "American Airlines Group"
        , "American Axle & Manufacturing"
        , "American Eagle Outfitters"
        , "American Electric Power"
        , "American Equity Investment Life Holding"
        , "American Express Company"
        , "American Express"
        , "American Family Insurance Group"
        , "American Financial Group"
        , "American International Group Incorporated"
        , "American National Group"
        , "American Tower"
        , "American Water Works"
        , "Americold Realty Trust"
        , "Ameriprise Financial"
        , "AmerisourceBergen Corporation"
        , "AmerisourceBergen"
        , "Ametek"
        , "Amgen"
        , "Amica Mutual Insurance"
        , "Amkor Technology"
        , "AMN Healthcare Services"
        , "Amphenol"
        , "Analog Devices"
        , "Andersons"
        , "Annaly Capital Management"
        , "Antero Resources"
        , "Anthem Incorporated"
        , "Anthem"
        , "Anywhere Real Estate"
        , "APA"
        , "APi Group"
        , "Apollo Global Management"
        , "Apple Incorporated"
        , "Apple"
        , "Applied Industrial Technologies"
        , "Applied Materials"
        , "AppLovin"
        , "AptarGroup"
        , "Aramark"
        , "ArcBest"
        , "Arch Resources"
        , "Archer Daniels Midland"
        , "Archer-Daniels-Midland Company"
        , "Arconic"
        , "Ares Management"
        , "Arista Networks"
        , "ARKO"
        , "Arrow Electronics"
        , "Arthur J. Gallagher"
        , "Asbury Automotive Group"
        , "ASGN"
        , "Ashland Global Holdings"
        , "Assurant"
        , "AT&T Incorporated"
        , "AT&T"
        , "ATI"
        , "Atkore"
        , "Atlas Air Worldwide Holdings"
        , "Atmos Energy"
        , "Auto-Owners Insurance"
        , "Autodesk"
        , "Autoliv"
        , "Automatic Data Processing"
        , "AutoNation"
        , "AutoZone"
        , "AvalonBay Communities"
        , "Avantor"
        , "Avaya Holdings"
        , "Avery Dennison"
        , "Avient"
        , "Avis Budget Group"
        , "Avnet"
        , "Baker Hughes"
        , "Ball"
        , "Bank of America Corporation"
        , "Bank of America"
        , "Bank of New York Mellon"
        , "Bath & Body Works"
        , "Baxter International"
        , "Beacon Roofing Supply"
        , "Beazer Homes USA"
        , "Becton Dickinson"
        , "Bed Bath & Beyond"
        , "Belden"
        , "Benchmark Electronics"
        , "Berkshire Hathaway Incorporated"
        , "Berkshire Hathaway"
        , "Berry Global Group"
        , "Best Buy Co., Incorporated"
        , "Best Buy"
        , "Big Lots"
        , "Bio-Rad Laboratories"
        , "Biogen"
        , "BJ's Wholesale Club"
        , "BlackRock"
        , "Blackstone"
        , "Block"
        , "Bloomin' Brands"
        , "BlueLinx Holdings"
        , "Boeing"
        , "Boise Cascade"
        , "Booking Holdings"
        , "Booz Allen Hamilton Holding"
        , "BorgWarner"
        , "Boston Properties"
        , "Boston Scientific"
        , "Boyd Gaming"
        , "Bread Financial Holdings"
        , "Bright Health Group"
        , "Brighthouse Financial"
        , "BrightView Holdings"
        , "Brink's"
        , "Brinker International"
        , "Bristol-Myers Squibb"
        , "Broadcom"
        , "Broadridge Financial Solutions"
        , "Brookdale Senior Living"
        , "Brown & Brown"
        , "Brown-Forman"
        , "Bruker"
        , "Brunswick"
        , "Builders FirstSource"
        , "Bunge Limited"
        , "Burlington Stores"
        , "BWX Technologies"
        , "C.H. Robinson Worldwide"
        , "Cabot"
        , "CACI International"
        , "Cadence Design Systems"
        , "Caesars Entertainment"
        , "Caleres"
        , "Callaway Golf"
        , "Calumet Specialty Products Partners"
        , "Campbell Soup"
        , "Camping World Holdings"
        , "Capital One Financial Corporation"
        , "Capital One Financial"
        , "Cardinal Health Incorporated"
        , "Cardinal Health"
        , "Carlisle"
        , "Carlyle Group"
        , "CarMax"
        , "Carrier Global"
        , "Carter's"
        , "Carvana"
        , "Casey's General Stores"
        , "Catalent"
        , "Caterpillar Incorporated"
        , "Caterpillar"
        , "Cboe Global Markets"
        , "CBRE Group"
        , "CDW"
        , "Celanese"
        , "Centene Corporation"
        , "Centene"
        , "CenterPoint Energy"
        , "Central Garden & Pet"
        , "Century Aluminum"
        , "Century Communities"
        , "Cerner"
        , "CF Industries Holdings"
        , "ChampionX"
        , "Change Healthcare"
        , "Charles River Laboratories International"
        , "Charles Schwab"
        , "Charter Communications Incorporated"
        , "Charter Communications"
        , "Cheesecake Factory"
        , "Chemed"
        , "Chemours"
        , "Cheniere Energy"
        , "Chesapeake Energy"
        , "Chevron Corporation"
        , "Chevron"
        , "Chewy"
        , "Chipotle Mexican Grill"
        , "CHS"
        , "Church & Dwight"
        , "Ciena"
        , "Cigna Corporation"
        , "Cigna"
        , "Cincinnati Financial"
        , "Cintas"
        , "Cisco Systems Incorporated"
        , "Cisco Systems"
        , "Citigroup Incorporated"
        , "Citigroup"
        , "Citizens Financial Group"
        , "Citrix Systems"
        , "Clean Harbors"
        , "Clear Channel Outdoor Holdings"
        , "Cleveland-Cliffs"
        , "Clorox"
        , "CME Group"
        , "CMS Energy"
        , "CNO Financial Group"
        , "Coca-Cola Consolidated"
        , "Coca-Cola"
        , "Cognizant Technology Solutions"
        , "Coinbase Global"
        , "Colgate-Palmolive"
        , "Columbia Sportswear"
        , "Comcast Corporation"
        , "Comcast"
        , "Comerica"
        , "Comfort Systems USA"
        , "Commercial Metals"
        , "CommScope Holding"
        , "Community Health Systems"
        , "Compass"
        , "Conagra Brands"
        , "Concentrix"
        , "Conduent"
        , "ConocoPhillips"
        , "Consolidated Edison"
        , "Constellation Brands"
        , "Continental Resources"
        , "Cooper Cos."
        , "Cooper-Standard Holdings"
        , "Copart"
        , "Core & Main"
        , "Cornerstone Building Brands"
        , "Corning"
        , "Corteva"
        , "Costco Wholesale Corporation"
        , "Costco Wholesale"
        , "Coterra Energy"
        , "Coty"
        , "Country Financial"
        , "Covetrus"
        , "Cowen"
        , "Cracker Barrel Old Country Store"
        , "Crane Holdings"
        , "Crestwood Equity Partners"
        , "Crocs"
        , "CrossAmerica Partners"
        , "Crown Castle International"
        , "Crown Holdings"
        , "CSX"
        , "Cummins"
        , "CUNA Mutual Group"
        , "Curtiss-Wright"
        , "CVS Health Corporation"
        , "CVS Health"
        , "D.R. Horton"
        , "Dana"
        , "Danaher"
        , "Darden Restaurants"
        , "Darling Ingredients"
        , "DaVita"
        , "DCP Midstream"
        , "Deckers Outdoor"
        , "Deere & Company"
        , "Deere"
        , "Delek US Holdings"
        , "Dell Technologies Incorporated"
        , "Dell Technologies"
        , "Delta Air Lines Incorporated"
        , "Delta Air Lines"
        , "Dentsply Sirona"
        , "Designer Brands"
        , "Devon Energy"
        , "DexCom"
        , "Diamondback Energy"
        , "Dick's Sporting Goods"
        , "Diebold Nixdorf"
        , "Digital Realty Trust"
        , "Dillard's"
        , "Discover Financial Services"
        , "DISH Network"
        , "DocuSign"
        , "Dollar General"
        , "Dollar Tree"
        , "Dominion Energy"
        , "Domino's Pizza"
        , "Domtar"
        , "Donaldson"
        , "DoorDash"
        , "Dover"
        , "Dow Incorporated"
        , "Dow"
        , "Dropbox"
        , "DTE Energy"
        , "Duke Energy"
        , "Dun & Bradstreet Holdings"
        , "DuPont"
        , "DXC Technology"
        , "Dycom Industries"
        , "E.W. Scripps"
        , "Eastman Chemical"
        , "eBay"
        , "Ecolab"
        , "Edison International"
        , "Edwards Lifesciences"
        , "Elanco Animal Health"
        , "Electronic Arts"
        , "Element Solutions"
        , "Eli Lilly"
        , "EMCOR Group"
        , "Emerson Electric"
        , "Encompass Health"
        , "Encore Wire"
        , "Endeavor Group Holdings"
        , "Energizer Holdings"
        , "Energy Transfer Limited Partnership"
        , "Energy Transfer"
        , "EnerSys"
        , "EnLink Midstream"
        , "Enovis"
        , "Ensign Group"
        , "Entegris"
        , "Entergy"
        , "Enterprise Products Partners Limited Partnership"
        , "Enterprise Products Partners"
        , "Envista Holdings"
        , "EOG Resources"
        , "EPAM Systems"
        , "EQT"
        , "Equifax"
        , "Equinix"
        , "Equitable Holdings"
        , "Equity Residential"
        , "Erie Insurance Group"
        , "Estée Lauder"
        , "Etsy"
        , "Euronet Worldwide"
        , "Evercore"
        , "Evergy"
        , "Eversource Energy"
        , "Exelon Corporation"
        , "Exelon"
        , "eXp World Holdings"
        , "Expedia Group"
        , "Expeditors Intl. of Washington"
        , "Exxon Mobil Corporation"
        , "Exxon Mobil"
        , "F5"
        , "Facebook Incorporated"
        , "Fannie Mae"
        , "Farmers Insurance Exchange"
        , "Fastenal"
        , "Federal Home Loan Mortgage Corporation"
        , "Federal National Mortgage Association"
        , "Federated Mutual Insurance"
        , "FedEx Corporation"
        , "FedEx"
        , "Fidelity National Financial"
        , "Fidelity National Information Services"
        , "Fifth Third Bancorp"
        , "First American Financial"
        , "First Horizon"
        , "First Republic Bank"
        , "First Solar"
        , "FirstEnergy"
        , "Fiserv"
        , "Five Below"
        , "Fleetcor Technologies"
        , "Floor & Decor Holdings"
        , "Flowers Foods"
        , "Flowserve"
        , "Fluor"
        , "FM Global"
        , "FMC"
        , "Food And Drinks Public Company Limited"
        , "Foot Locker"
        , "Ford Motor Company"
        , "Ford Motor"
        , "Fortinet"
        , "Fortive"
        , "Fortune Brands Home & Security"
        , "Fox"
        , "Franchise Group"
        , "Franklin Resources"
        , "Freddie Mac"
        , "Freeport-McMoRan"
        , "Frontier Communications"
        , "FTI Consulting"
        , "G-III Apparel Group"
        , "GameStop"
        , "Gannett"
        , "Gap"
        , "Garrett Motion"
        , "Gartner"
        , "Generac Holdings"
        , "General Dynamics Corporation"
        , "General Dynamics"
        , "General Electric Company"
        , "General Electric"
        , "General Mills"
        , "General Motors Company"
        , "General Motors"
        , "Genesco"
        , "Genesis Energy"
        , "Genuine Parts"
        , "Genworth Financial"
        , "GEO Group"
        , "Gilead Sciences"
        , "Global Partners"
        , "Global Payments"
        , "Globe Life"
        , "GMS"
        , "GoDaddy"
        , "Goldman Sachs Group"
        , "Goodyear Tire & Rubber"
        , "Graham Holdings"
        , "Granite Construction"
        , "Graphic Packaging Holding"
        , "Gray Television"
        , "Graybar Electric"
        , "Green Plains"
        , "Greif"
        , "Griffon"
        , "Grocery Outlet Holding"
        , "Group 1 Automotive"
        , "Guardian Life Ins. Co. of America"
        , "Guess"
        , "GXO Logistics"
        , "H&R Block"
        , "H.B. Fuller"
        , "Halliburton"
        , "Hanesbrands"
        , "Hanover Insurance Group"
        , "Harley-Davidson"
        , "Harsco"
        , "Hartford Financial Services Group"
        , "Hasbro"
        , "Hawaiian Electric Industries"
        , "HCA Healthcare Incorporated"
        , "HCA Healthcare"
        , "Henry Schein"
        , "Hershey"
        , "Hertz Global Holdings"
        , "Hess"
        , "Hewlett Packard Enterprise"
        , "Hewlett-Packard Company Incorporated (HP)"
        , "HF Sinclair"
        , "Hill-Rom Holdings"
        , "Hillenbrand"
        , "Hilton Grand Vacations"
        , "Hilton Worldwide Holdings"
        , "HNI"
        , "Hologic"
        , "Home Depot"
        , "Honeywell International Incorporated"
        , "Honeywell International"
        , "Hormel Foods"
        , "Host Hotels & Resorts"
        , "Hovnanian Enterprises"
        , "Howmet Aerospace"
        , "Hub Group"
        , "Hubbell"
        , "Humana Incorporated"
        , "Humana"
        , "Huntington Bancshares"
        , "Huntington Ingalls Industries"
        , "Huntsman"
        , "Hyatt Hotels"
        , "Hyster-Yale Materials Handling"
        , "IAC/InterActiveCorp"
        , "IBM"
        , "Icahn Enterprises"
        , "IDEX"
        , "IDEXX Laboratories"
        , "iHeartMedia"
        , "II-VI"
        , "Illinois Tool Works"
        , "Illumina"
        , "Incyte"
        , "Ingersoll Rand"
        , "Ingles Markets"
        , "Ingram Micro Incorporated"
        , "Ingredion"
        , "Insight Enterprises"
        , "Insperity"
        , "Intel Corporation"
        , "Intel"
        , "Interactive Brokers Group"
        , "Intercontinental Exchange"
        , "International Business Machines Corporation"
        , "International Flavors & Fragrances"
        , "International Paper"
        , "Interpublic Group"
        , "Intuit"
        , "Intuitive Surgical"
        , "IQVIA Holdings"
        , "Iron Mountain"
        , "Island Heat Fashions"
        , "ITT"
        , "J.B. Hunt Transport Services"
        , "J.M. Smucker"
        , "Jabil"
        , "Jackson Financial"
        , "Jacobs Engineering Group"
        , "Jefferies Financial Group"
        , "JELD-WEN Holding"
        , "JetBlue Airways"
        , "Joann"
        , "Johnson & Johnson"
        , "Jones Financial (Edward Jones)"
        , "Jones Lang LaSalle"
        , "JPMorgan Chase & Company"
        , "JPMorgan Chase"
        , "Juniper Networks"
        , "Kaiser Aluminum"
        , "Kar Auction Services"
        , "KB Home"
        , "KBR"
        , "Kellogg"
        , "Kelly Services"
        , "Kemper"
        , "Keurig Dr Pepper"
        , "KeyCorp"
        , "Keysight Technologies"
        , "Kimberly-Clark"
        , "Kinder Morgan"
        , "Kirby"
        , "KKR"
        , "KLA"
        , "Knight-Swift Transportation Holdings"
        , "Knights of Columbus"
        , "Kohl's"
        , "Kontoor Brands"
        , "Kraft Heinz"
        , "Kroger"
        , "L3Harris Technologies"
        , "Laboratory Corp. of America"
        , "Lam Research"
        , "Lamb Weston Holdings"
        , "Land O'Lakes"
        , "Landstar System"
        , "Las Vegas Sands"
        , "LCI Industries"
        , "Lear"
        , "Leggett & Platt"
        , "Leidos Holdings"
        , "Lennar"
        , "Lennox International"
        , "Levi Strauss"
        , "LGI Homes"
        , "LHC Group"
        , "Liberty Energy"
        , "Liberty Media"
        , "Liberty Mutual Insurance Group"
        , "Light & Wonder"
        , "Lincoln Electric Holdings"
        , "Lincoln National"
        , "Lithia Motors"
        , "Live Nation Entertainment"
        , "LKQ"
        , "loanDepot"
        , "Lockheed Martin Corporation"
        , "Lockheed Martin"
        , "Loews"
        , "Louisiana-Pacific"
        , "Lowe's Companies Incorporated"
        , "Lowe's"
        , "LPL Financial Holdings"
        , "Lululemon athletica"
        , "Lumen Technologies"
        , "Lyft"
        , "M&T Bank"
        , "M/I Homes"
        , "Macy's"
        , "Magellan Midstream Partners"
        , "ManpowerGroup"
        , "ManTech International"
        , "Marathon Oil"
        , "Marathon Petroleum Corporation"
        , "Marathon Petroleum"
        , "Markel"
        , "Marriott International"
        , "Marriott Vacations Worldwide"
        , "Marsh & McLennan"
        , "Martin Marietta Materials"
        , "Marvell Technology"
        , "Masco"
        , "Massachusetts Mutual Life Insurance"
        , "MasTec"
        , "Mastercard"
        , "Match Group"
        , "Matson"
        , "Mattel"
        , "Mattress Firm Group"
        , "Maxim Integrated Products"
        , "Maximus"
        , "McAfee"
        , "McCormick"
        , "McDonald's"
        , "McKesson Corporation"
        , "McKesson"
        , "MDC Holdings"
        , "MDU Resources Group"
        , "Medical Mutual of Ohio"
        , "Merck & Company Incorporated"
        , "Merck"
        , "Mercury General"
        , "Meritage Homes"
        , "Meritor"
        , "Meta Platforms"
        , "MetLife Incorporated"
        , "MetLife"
        , "Mettler-Toledo International"
        , "MGM Resorts International"
        , "Microchip Technology"
        , "Micron Technology"
        , "Microsoft Corporation"
        , "Microsoft"
        , "Middleby"
        , "MillerKnoll"
        , "MKS Instruments"
        , "Moderna"
        , "Mohawk Industries"
        , "Molina Healthcare"
        , "Molson Coors Beverage"
        , "Mondelez International"
        , "Monster Beverage"
        , "Moody's"
        , "Moog"
        , "Morgan Stanley"
        , "Mosaic"
        , "Motorola Solutions"
        , "Mr. Cooper Group"
        , "MRC Global"
        , "MSC Industrial Direct"
        , "Mueller Industries"
        , "Murphy Oil"
        , "Murphy USA"
        , "Mutual of America Life Insurance"
        , "Mutual of Omaha Insurance"
        , "MYR Group"
        , "Nasdaq"
        , "Nationwide"
        , "Navient"
        , "NCR"
        , "NetApp"
        , "Netflix"
        , "New Jersey Resources"
        , "New Residential Investment"
        , "New York Life Insurance"
        , "Newell Brands"
        , "Newmark Group"
        , "NewMarket"
        , "Newmont"
        , "News Corp."
        , "Nexstar Media Group"
        , "NextEra Energy"
        , "NGL Energy Partners"
        , "NIKE Incorporated"
        , "Nike"
        , "NiSource"
        , "NLV Financial"
        , "Nordson"
        , "Nordstrom"
        , "Norfolk Southern"
        , "Northern Trust"
        , "Northrop Grumman Corporation"
        , "Northrop Grumman"
        , "Northwestern Mutual"
        , "NortonLifeLock"
        , "NOV"
        , "NRG Energy"
        , "Nu Skin Enterprises"
        , "Nucor"
        , "Nvidia"
        , "NVR"
        , "O'Reilly Automotive"
        , "O-I Glass"
        , "Occidental Petroleum"
        , "ODP"
        , "OGE Energy"
        , "Ohio National Mutual"
        , "Old Dominion Freight Line"
        , "Old Republic International"
        , "Olin"
        , "Olympic Steel"
        , "Omnicom Group"
        , "ON Semiconductor"
        , "OneMain Holdings"
        , "Oneok"
        , "Opendoor Technologies"
        , "Option Care Health"
        , "Oracle Corporation"
        , "Oracle"
        , "Oshkosh"
        , "Otis Worldwide"
        , "Overstock.com"
        , "Ovintiv"
        , "Owens & Minor"
        , "Owens Corning"
        , "Paccar"
        , "Pacific Life"
        , "Packaging Corp. of America"
        , "Palo Alto Networks"
        , "Par Pacific Holdings"
        , "Paramount Global"
        , "Parker-Hannifin"
        , "Parsons"
        , "Party City Holdco"
        , "Patrick Industries"
        , "Patterson"
        , "Paychex"
        , "PayPal Holdings"
        , "PBF Energy"
        , "PC Connection"
        , "Peabody Energy"
        , "Peloton Interactive"
        , "Penn Mutual Life Insurance"
        , "Penn National Gaming"
        , "PennyMac Financial Services"
        , "Penske Automotive Group"
        , "PepsiCo Incorporated"
        , "PepsiCo"
        , "Performance Food Group"
        , "PerkinElmer"
        , "Petco Health and Wellness"
        , "Peter Kiewit Sons'"
        , "Pfizer Incorporated"
        , "Pfizer"
        , "PG&E"
        , "Philip Morris International"
        , "Phillips 66"
        , "Pinnacle West Capital"
        , "Pinterest"
        , "Pioneer Natural Resources"
        , "Pitney Bowes"
        , "Plains All American Pipeline Limited Partnership"
        , "Plains GP Holdings Limited Partnership"
        , "Plains GP Holdings"
        , "Playtika Holding"
        , "Plexus"
        , "PNC Financial Services Group"
        , "Polaris"
        , "Pool"
        , "Popular"
        , "Portland General Electric"
        , "Post Holdings"
        , "PPG Industries"
        , "PPL"
        , "PriceSmart"
        , "Primerica"
        , "Primoris Services"
        , "Principal Financial"
        , "Procter & Gamble Company"
        , "Procter & Gamble"
        , "PROG Holdings"
        , "Progressive Corporation"
        , "Progressive"
        , "Prologis"
        , "Prudential Financial Incorporated"
        , "Prudential Financial"
        , "Public Service Enterprise Group"
        , "Public Storage"
        , "Publix Super Markets"
        , "Puget Energy"
        , "PulteGroup"
        , "Pure Storage"
        , "PVH"
        , "Qorvo"
        , "Quad/Graphics"
        , "Qualcomm"
        , "Quanta Services"
        , "Quest Diagnostics"
        , "Qurate Retail"
        , "R.R. Donnelley & Sons"
        , "Rackspace Technology"
        , "Ralph Lauren"
        , "Range Resources"
        , "Raymond James Financial"
        , "Raytheon Technologies"
        , "Regal Rexnord"
        , "Regeneron Pharmaceuticals"
        , "Regions Financial"
        , "Reinsurance Group of America"
        , "Reliance Steel & Aluminum"
        , "Renewable Energy Group"
        , "Rent-A-Center"
        , "Republic Services"
        , "Resideo Technologies"
        , "ResMed"
        , "Resolute Forest Products"
        , "REV Group"
        , "RH"
        , "Rite Aid"
        , "Robert Half International"
        , "Rocket Companies"
        , "Rockwell Automation"
        , "Roku"
        , "Rollins"
        , "Roper Technologies"
        , "Ross Stores"
        , "RPM International"
        , "Rush Enterprises"
        , "Ryder System"
        , "Ryerson Holding"
        , "S&P Global"
        , "Saia"
        , "Salesforce"
        , "Sally Beauty Holdings"
        , "Sanderson Farms"
        , "Sanmina"
        , "SBA Communications"
        , "ScanSource"
        , "Schlumberger NV"
        , "Schneider National"
        , "Schnitzer Steel Industries"
        , "Science Applications International"
        , "Scotts Miracle-Gro"
        , "Seaboard"
        , "Sealed Air"
        , "Securian Financial Group"
        , "Select Medical Holdings"
        , "Selective Insurance Group"
        , "Sempra"
        , "Sentry Insurance Group"
        , "Service Corp. International"
        , "ServiceNow"
        , "Sherman Williams"
        , "Sherwin-Williams"
        , "Signature Bank"
        , "Silgan Holdings"
        , "Simon Property Group"
        , "Sinclair Broadcast Group"
        , "SiteOne Landscape Supply"
        , "Skechers U.S.A."
        , "SkyWest"
        , "Skyworks Solutions"
        , "Sleep Number"
        , "SLM"
        , "SM Energy"
        , "Snap"
        , "Snap-on"
        , "Sonic Automotive"
        , "Sonoco Products"
        , "Southern"
        , "Southwest Airlines"
        , "Southwest Gas Holdings"
        , "Southwestern Energy"
        , "SpartanNash"
        , "Spectrum Brands Holdings"
        , "Spire"
        , "Spirit AeroSystems Holdings"
        , "Spirit Airlines"
        , "Splunk"
        , "Sprague Resources"
        , "Sprint Corporation"
        , "Sprouts Farmers Market"
        , "SS&C Technologies Holdings"
        , "Stanley Black & Decker"
        , "Starbucks"
        , "State Farm Insurance"
        , "State Street"
        , "Steel Dynamics"
        , "Steelcase"
        , "Stepan"
        , "Stericycle"
        , "Stewart Information Services"
        , "Stifel Financial"
        , "StoneX Group Incorporated"
        , "StoneX Group"
        , "Stryker"
        , "Summit Materials"
        , "Sun Communities"
        , "Super Micro Computer"
        , "Surgery Partners"
        , "SVB Financial Group"
        , "Synchrony Financial"
        , "Syneos Health"
        , "Synopsys"
        , "Sysco Corporation"
        , "Sysco"
        , "T-Mobile US Incorporated"
        , "T. Rowe Price"
        , "Take-Two Interactive Software"
        , "Tapestry"
        , "Targa Resources"
        , "Target Corporation"
        , "Target"
        , "Taylor Morrison Home"
        , "TD Synnex"
        , "TEGNA"
        , "Teledyne Technologies"
        , "Teleflex"
        , "Telephone & Data Systems"
        , "Tempur Sealy International"
        , "Tenet Healthcare"
        , "Tenneco"
        , "Teradyne"
        , "Terex"
        , "Tesla"
        , "Tetra Tech"
        , "Texas Instruments"
        , "Texas Roadhouse"
        , "Textron"
        , "The Allstate Corporation"
        , "The Boeing Company"
        , "The Coca-Cola Company"
        , "The Goldman Sachs Group Incorporated"
        , "The Home Depot Incorporated"
        , "The Kroger Company"
        , "The TJX Cos., Incorporated"
        , "The Walt Disney Company"
        , "Thermo Fisher Scientific"
        , "Thor Industries"
        , "Thrivent Financial for Lutherans"
        , "TIAA"
        , "Timken"
        , "TJX"
        , "Toll Brothers"
        , "TopBuild"
        , "Toro"
        , "TPG"
        , "Tractor Supply"
        , "TransDigm Group"
        , "TransUnion"
        , "Travel + Leisure"
        , "TravelCenters of America"
        , "Travelers"
        , "TreeHouse Foods"
        , "Tri Pointe Homes"
        , "Trimble"
        , "TriNet Group"
        , "TrueBlue"
        , "Truist Financial"
        , "TTEC Holdings"
        , "TTM Technologies"
        , "Tutor Perini"
        , "Twilio"
        , "Twitter"
        , "Tyson Foods Incorporated"
        , "Tyson Foods"
        , "U.S. Bancorp"
        , "Uber Technologies"
        , "UFP Industries"
        , "UGI"
        , "Ulta Beauty"
        , "Under Armour"
        , "Union Pacific"
        , "United Airlines Holdings Incorporated"
        , "United Airlines Holdings"
        , "United Natural Foods"
        , "United Parcel Service Incorporated"
        , "United Rentals"
        , "United States Steel"
        , "UnitedHealth Group Incorporated"
        , "UnitedHealth Group"
        , "Univar Solutions"
        , "Universal Health Services"
        , "Univision Communciations"
        , "Unum Group"
        , "UPS"
        , "Urban Outfitters"
        , "US Foods Holding"
        , "USAA"
        , "UWM Holdings"
        , "Valero Energy Corporation"
        , "Valero Energy"
        , "Valhi"
        , "Valmont Industries"
        , "Valvoline"
        , "Ventas"
        , "Verisk Analytics"
        , "Veritiv"
        , "Verizon Communications Incorporated"
        , "Verizon Communications"
        , "Vertex Pharmaceuticals"
        , "Vertiv Holdings"
        , "VF"
        , "Viasat"
        , "Viatris"
        , "Victoria's Secret"
        , "Virtu Financial"
        , "Visa"
        , "Vishay Intertechnology"
        , "Vista Outdoor"
        , "Visteon"
        , "Vistra"
        , "Vizio Holding"
        , "Vontier"
        , "Voya Financial"
        , "Vroom"
        , "Vulcan Materials"
        , "W.R. Berkley"
        , "W.W. Grainger"
        , "Walgreens Boots Alliance Incorporated"
        , "Walgreens Boots Alliance"
        , "Walmart Incorporated"
        , "Walmart"
        , "Walt Disney"
        , "Warner Bros. Discovery"
        , "Warner Music Group"
        , "Waste Management"
        , "Waters"
        , "Watsco"
        , "Wayfair"
        , "WEC Energy Group"
        , "Weis Markets"
        , "Wells Fargo & Company"
        , "Wells Fargo"
        , "Welltower"
        , "Werner Enterprises"
        , "WESCO International"
        , "West Pharmaceutical Services"
        , "Western & Southern Financial Group"
        , "Western Digital"
        , "Western Midstream Partners"
        , "Western Union"
        , "Westinghouse Air Brake Technologies"
        , "Westlake"
        , "WestRock"
        , "WeWork"
        , "Weyerhaeuser"
        , "Whirlpool"
        , "Williams"
        , "Williams-Sonoma"
        , "Winnebago Industries"
        , "Wolverine World Wide"
        , "Woodward"
        , "Workday"
        , "World Fuel Services Corporation"
        , "World Fuel Services"
        , "Worthington Industries"
        , "Wynn Resorts"
        , "Xcel Energy"
        , "Xerox Holdings"
        , "Xilinx"
        , "XPO Logistics"
        , "Xylem"
        , "Yellow"
        , "Yum Brands"
        , "Yum China Holdings"
        , "Zebra Technologies"
        , "Zillow Group"
        , "Zimmer Biomet Holdings"
        , "Zions Bancorp."
        , "Zoetis"
        , "Zoom Video Communications"
        , "Zynga"
        ,
         ]
    y = choice(xo)
    return y

if __name__ == '__main__':
    print(rand_company_name())
    print('example: \nimport pyGenRandCompanyName as ran_co\n\nprint(ran_co.rand_company_name())\n')