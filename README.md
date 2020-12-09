# KGIS
Public Spatial Data from Karnataka Geographic Information System - ಕರ್ನಾಟಕ ಭೌಗೋಳಿಕ ಮಾಹಿತಿ ವ್ಯವಸ್ಥೆ

_______________________

This project is used to download the spatial data shapefiles from the KGIS portal and convert them to cleaned, combined and zipped geopackage files for the following layers. The script `fetch-kgis-data.py` is used to fetch the data.

## Data Layers

```python
1. Assembly Constituency Boundaries
2. Parliment Constituency Boundaries
3. Village Boundaries
4. Hobli Boundaries
5. Wards (town) Boundaries
6. Town Boundaries
7. Taluk Boundaries
8. District Boundaries
9. State Boundary
```

## Environment

Before running the script, set up the environment by running `pip install -r requirements.txt` from within the repository root directory.

Make sure the Unrar and Unzip tools are installed in your system.

On linux:

```bash
sudo apt-get install unrar unzip
```

On MacOS:

```bash
brew install unrar unzip
```

----------------------
## Run the Script

```bash
python fetch-kgis-data.py
```

The script downloads the compressed files into the `./data/raw` directory which are then cleaned, combined and zipped to `/data/output` directory.

## Author

Nikhil S Hubballi 

[Mail](mailto:nikhil@samashti.tech) | [LinkedIn](https://www.linkedin.com/in/nikhilhubballi/) | [Twitter](https://twitter.com/samashti_)

______________________

```bash
├──
├── [4.0K]  data
│   ├── [4.0K]  output
│   │   ├── [7.6M]  AC_Boundaries.gpkg.zip      
│   │   ├── [4.1M]  District_Boundaries.gpkg.zip
│   │   ├── [ 15M]  Hobli_Boundaries.gpkg.zip   
│   │   ├── [3.6M]  PC_Boundaries.gpkg.zip      
│   │   ├── [577K]  State_Boundaries.gpkg.zip   
│   │   ├── [8.4M]  Taluk_Boundaries.gpkg.zip   
│   │   ├── [2.1M]  Town_Boundaries.gpkg.zip    
│   │   ├── [ 64M]  Village_Boundaries.gpkg.zip 
│   │   └── [8.5M]  Ward_Boundaries.gpkg.zip    
│   └── [4.0K]  raw
│       ├── [6.4M]  AC_Boundary.rar
│       ├── [3.5M]  District.rar
│       ├── [ 13M]  Hobli.rar
│       ├── [2.9M]  PC_Boundary.rar
│       ├── [480K]  State.rar
│       ├── [7.2M]  Taluk.rar
│       ├── [4.0K]  towns
│       │   ├── [ 88K]  Bagalkot.rar
│       │   ├── [197K]  Ballari.rar
│       │   ├── [234K]  Belagavi.rar
│       │   ├── [ 30K]  Bengaluru%20(Rural).rar 
│       │   ├── [101K]  Bengaluru%20(Urban).rar 
│       │   ├── [ 50K]  Bidar.rar
│       │   ├── [ 55K]  Chamarajanagara.rar     
│       │   ├── [ 32K]  Chikkaballapura.rar     
│       │   ├── [ 71K]  Chikkamagaluru.rar      
│       │   ├── [ 32K]  Chitradurga.rar
│       │   ├── [116K]  Dakshina%20Kannada.rar  
│       │   ├── [ 30K]  Davanagere.rar
│       │   ├── [ 34K]  Dharwad.rar
│       │   ├── [ 56K]  Gadag.rar
│       │   ├── [ 73K]  Hassan.rar
│       │   ├── [ 47K]  Haveri.rar
│       │   ├── [ 59K]  Kalburgi.rar
│       │   ├── [ 25K]  Kodagu.rar
│       │   ├── [ 59K]  Kolara.rar
│       │   ├── [ 67K]  Koppal.rar
│       │   ├── [ 83K]  Mandya.rar
│       │   ├── [ 90K]  Mysuru.rar
│       │   ├── [ 69K]  Raichur.rar
│       │   ├── [ 54K]  Ramanagara.rar
│       │   ├── [ 60K]  Shivamogga.rar
│       │   ├── [ 67K]  Tumakuru.rar
│       │   ├── [ 39K]  Udupi.rar
│       │   ├── [123K]  Uttara%20Kannada.rar
│       │   ├── [ 93K]  Vijayapura.rar
│       │   └── [ 56K]  Yadgir.rar
│       ├── [4.0K]  villages
│       │   ├── [2.6M]  Bagalakote.zip
│       │   ├── [4.4M]  Ballari.zip
│       │   ├── [6.3M]  Belagavi.zip
│       │   ├── [3.5M]  Bengaluru%20(Rural).zip
│       │   ├── [3.4M]  Bengaluru%20(Urban).zip
│       │   ├── [2.7M]  Bidar.zip
│       │   ├── [2.6M]  Chamarajanagara.zip
│       │   ├── [5.2M]  Chikkaballapura.zip
│       │   ├── [4.2M]  Chikkamagaluru.zip
│       │   ├── [3.7M]  Chitradurga.zip
│       │   ├── [2.3M]  Dakshina%20Kannada.zip
│       │   ├── [2.9M]  Davanagere.zip
│       │   ├── [2.3M]  Dharwad.zip
│       │   ├── [1.7M]  Gadag.zip
│       │   ├── [8.2M]  Hassan.zip
│       │   ├── [3.0M]  Haveri.zip
│       │   ├── [3.6M]  Kalburgi.zip
│       │   ├── [3.0M]  Kodagu.zip
│       │   ├── [5.5M]  Kolara.zip
│       │   ├── [2.5M]  Koppal.zip
│       │   ├── [6.0M]  Mandya.zip
│       │   ├── [5.4M]  Mysuru.zip
│       │   ├── [3.7M]  Raichur.zip
│       │   ├── [3.1M]  Ramanagara.zip
│       │   ├── [5.3M]  Shivamogga.zip
│       │   ├── [9.3M]  Tumakuru.zip
│       │   ├── [1.6M]  Udupi.zip
│       │   ├── [4.8M]  Uttara%20Kannada.zip
│       │   ├── [3.2M]  Vijayapura.zip
│       │   └── [2.2M]  Yadgir.zip
│       └── [4.0K]  wards
│           ├── [490K]  Bagalkot.rar
│           ├── [658K]  Ballari.rar
│           ├── [1.1M]  Belagavi.rar
│           ├── [153K]  Bengaluru%20(Rural).rar
│           ├── [843K]  Bengaluru%20(Urban).rar
│           ├── [266K]  Bidar.rar
│           ├── [180K]  Chamarajanagara.rar
│           ├── [171K]  Chikkaballapura.rar
│           ├── [297K]  Chikkamagaluru.rar
│           ├── [127K]  Chitradurga.rar
│           ├── [547K]  Dakshina%20Kannada.rar
│           ├── [109K]  Davanagere.rar
│           ├── [262K]  Dharwad.rar
│           ├── [275K]  Gadag.rar
│           ├── [344K]  Hassan.rar
│           ├── [263K]  Haveri.rar
│           ├── [382K]  Kalburgi.rar
│           ├── [112K]  Kodagu.rar
│           ├── [279K]  Kolara.rar
│           ├── [277K]  Koppal.rar
│           ├── [334K]  Mandya.rar
│           ├── [522K]  Mysuru.rar
│           ├── [483K]  Raichur.rar
│           ├── [330K]  Ramanagara.rar
│           ├── [299K]  Shivamogga.rar
│           ├── [433K]  Tumakuru.rar
│           ├── [220K]  Udupi.rar
│           ├── [447K]  Uttara%20Kannada.rar
│           ├── [396K]  Vijayapura.rar
│           └── [282K]  Yadgir.rar
├──
```
