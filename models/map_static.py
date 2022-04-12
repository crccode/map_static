# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 
import base64
import requests
class map_static(models.Model): 
    _name = 'ej.map_static' 
    name = fields.Char(string='name') 
 
    latitud = fields.Float(string='latitud',digits=(12, 10))

    longitud = fields.Float(string='longitud',digits=(12, 10))
 
    size = fields.Char(string='size') 
 
    zoom = fields.Integer(string='zoom') 
 
    map_type = fields.Char(string='Tipo de mapa')
    # state = fields.Selection(string="", selection=[('', ''), ('', ''), ], required=False, )
 
    marker_color = fields.Char(string='Color Marcador')
 
    marker_label = fields.Char(string='marker_label') 
 
    marker_point = fields.Char(string='marker_point')

    def mapa_pdf(self):
        lat = self.latitud
        lng = self.longitud
        # self.manzana
        api_key = "AIzaSyDuRB47xeByJio9d8KEDW41xnA5E-C3xFg"
        # api_key = "AIzaSyBDaeWicvigtP9xPv919E-RNoxfvC"
        # AIzaSyBDaeWicvigtP9xPv919E - RNoxfvC - Hqik & callback = iniciarMap
        url = "https://maps.googleapis.com/maps/api/staticmap?"

        center ="-15.800513,-47.91378" #"Dehradun"
        # center = str(lat) + "," + str(lng)
        size = "900x1280"
        zoom = 18
        map_type = "satellite"
        # url = url + "center=" + center + "&zoom=" + str(
        #     zoom) + "&size=" + size + "&maptype=" + map_type + "&key=" + api_key + "&sensor=false"

        marker_color = "color:blue"
        marker_label = "S"
        marker_point = "7C" + center

        url = url + "center=" + center + "&zoom=" +str(zoom) + "&size="+ size + "&markers="+marker_color+"%7Clabel:"+ marker_label+"%"+marker_point+ "&maptype="+ map_type + "&key=" +api_key + "&sensor=false"

        my_html = 'data:image/png;base64, {}'.format(base64.b64encode(requests.get(url).content).decode('utf-8'))

        return my_html
