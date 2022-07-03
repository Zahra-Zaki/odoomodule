from odoo import models,fields,api



class Travel(models.Models):
    _name='travel.travel'

    name= fields.Char(string="Name")
    destination=fields.Char(string="Destintion")
    start_data=fields.data(string="Start Data")
    end_data=fileds.Data(string="End Data")