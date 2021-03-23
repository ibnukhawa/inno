{
  'name': 'Innograph Warranty Serial Number',
  'author': 'Innograph Odoo Developers',
  'version': '1.0',
  'depends': [
    'sale','product','mrp','serial_pabrik'
  ],
  'data': [
    'views/inno_serial_number.xml',
    'report/barcode.xml', 
    'security/ir.model.access.csv',
    'data/inno_serial_number_sequence.xml'
  ],
  'qweb': [
    # 'static/src/xml/nama_widget.xml',
  ],
  'sequence': 1,
  'auto_install': False,
  'installable': True,
  'application': True,
  'category': 'Sales Warranty',
  'summary': 'by Ibnu Nur Khawarizmi & Bayu Dwi Saputra',
  'license': 'OPL-1',
  'website': 'https://www.innograph.com/',
  'description': '-'
}