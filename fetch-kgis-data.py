# imports
import os
# import json
import shutil
import requests
from glob import glob

import pandas as pd
import geopandas as gpd
# from tqdm import tqdm
from rich.progress import track
from bs4 import BeautifulSoup as bs4

from zipfile import ZipFile, ZIP_DEFLATED
from pyunpack import Archive

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def download_link(link, path):
    """ """
    filename = os.path.basename(link)
    create_dir(path)

    data = requests.get(link, stream=True)

    if data.status_code == 200:
        with open(os.path.join(path, filename), 'wb') as f:
            for chunk in data.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    f.flush()            
        return True
    else:
        return False


def extract(file, path):
    """ """
    # dependencies: need patool and unrar in the system
    create_dir(path)
    return Archive(file).extractall(path)


def create_dir(path):
    """ """
    if not os.path.exists(path):
        os.makedirs(path)


def compress(file):
    """ """
    outname = file.replace('.gpkg', '.gpkg.zip')
    with ZipFile(outname, mode='w', compression=ZIP_DEFLATED) as zf:
        zf.write(file)
    if os.path.exists(outname):
        os.remove(file)


def get_links(url):
    """ """
    try:
        response = requests.get(url)
        assert(response.status_code == 200), 'Status Error'
        html = bs4(response.content, 'lxml')
        links = [a.get('href') for a in html.findAll('a')]
        links = [base_url+l for l in links if not l.endswith('/')]
        return links
    except:
        print("Could not fetch the links from the url")
        return list()


def convert_to_gpkg(path, filename):
    """ """
    files = glob(f'{path}/*.shp')
    gdf = pd.concat([gpd.read_file(f) for f in files])
    gdf = gdf.to_crs({'init': 'EPSG:4326'})
    gdf.to_file(os.path.join(out, filename), driver='GPKG')


def main():
    """ """
    # fetch admin bpundary vector file
    links = get_links(base_url + admin)
    links += [ac, pc]

    _ = [download_link(link, raw) for link in track(
            links, 
            description='Downloading admin boundary file links...'
        )]

    rars = glob(f'{raw}/*.rar')

    for rar in track(
        rars,
        description='Extracting and generating outputs for admin boundaries...'
    ):
        extract(rar, rartmp)
        convert_to_gpkg(
            rartmp, 
            (os.path.basename(rar)
                    .replace('_Boundary', '')
                    .replace('.rar', '_Boundaries.gpkg'))
        )
        shutil.rmtree(rartmp)

    # fetch village boundary vector file
    links = get_links(base_url + villages)

    _ = [download_link(link, vpath) for link in track(
            links, 
            description='Downloading village boundary file links...'
        )]

    zips = glob(f'{vpath}/*.zip')
    _ = [extract(f, ziptmp) for f in track(
            zips, 
            description='Extracting files for village boundaries...'
        )]

    convert_to_gpkg(ziptmp, 'Village_Boundaries.gpkg')
    shutil.rmtree(ziptmp)

    # fetch town boundary vector file
    links = get_links(base_url + towns)

    _ = [download_link(link, tpath) for link in track(
            links, 
            description='Downloading links for town boundary files...'
        )]

    rars = glob(f'{tpath}/*.rar')
    _ = [extract(f, rartmp) for f in track(
            rars, 
            description='Extracting files for town boundaries (P1)...'
        )]

    zips = glob(f'{rartmp}/*/*.zip')
    _ = [extract(f, ziptmp) for f in track(
            zips, 
            description='Extracting files for town boundaries (P2)...'
        )]

    convert_to_gpkg(ziptmp, 'Town_Boundaries.gpkg')
    shutil.rmtree(ziptmp)
    shutil.rmtree(rartmp)

    # fetch ward boundary vector file
    links = get_links(base_url + wards)

    _ = [download_link(link, wpath) for link in track(
            links, 
            description='Downloading ward boundary file links...'
        )]

    rars = glob(f'{wpath}/*.rar')
    _ = [extract(f, rartmp) for f in track(
            rars, 
            description='Extracting files for ward boundaries (P1)...'
        )]

    zips = glob(f'{rartmp}/*/*.zip')
    _ = [extract(f, ziptmp) for f in track(
            zips, 
            description='Extracting files for ward boundaries (P2)...'
        )]

    convert_to_gpkg(ziptmp, 'Ward_Boundaries.gpkg')
    shutil.rmtree(ziptmp)
    shutil.rmtree(rartmp)

    outfiles = glob(f'{out}/*.gpkg')
    _ = [compress(f) for f in track(outfiles, description='Compressing Outputs...')]


if __name__ == "__main__":

    base_url = 'https://kgis.ksrsac.in'
    admin = '/kgisdocuments/PDF_KML_SHP/Shapefiles/m-shp'
    villages = '/kgisdocuments/PDF_KML_SHP/Shapefiles/shp'
    towns = '/kgisdocuments/PDF_KML_SHP/Town/Shapefile/'
    wards = '/kgisdocuments/PDF_KML_SHP/Ward/Shapefile/'
    ac = 'https://kgis.ksrsac.in/kgis/kgisdocuments/Election%20Boundaries/AC_Boundary.rar'
    pc = 'https://kgis.ksrsac.in/kgis/kgisdocuments/Election%20Boundaries/PC_Boundary.rar'

    # set up paths and folders.
    raw = './data/raw'
    create_dir(raw)

    out = './data/output'
    create_dir(out)

    tpath = os.path.join(raw, 'towns')
    wpath = os.path.join(raw, 'wards')
    vpath = os.path.join(raw, 'villages')

    # temp folders for extracting files.
    rartmp = os.path.join(raw, 'rartmp')
    ziptmp = os.path.join(raw, 'ziptmp')

    main()
