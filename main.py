import xml.etree.ElementTree as ET
import Product

orders = {}

def parseProducts():
    products_xml = ET.parse("Products.xml")
    products_root = products_xml.getroot()

    for product_xml in products_root.findall("Order"):
        product_type = int(product_xml.get("type"))
        product = Product(product_type, product_xml)
        orders[product_type] = product

def main():
    parseProducts()

if __name__ == "main":
    main()