import zipfile
from lxml import etree
import argparse
import os.path
import subprocess
import re

# Renoise XML contains a "Filename" field that is wrong. Instead of using
# it, try to guess which file to use.
def guess_file_name(name):
    pass

def renoise_manifest_path(dirname):
    return os.path.join(dirname, 'Instrument.xml')

def bitwig_manifest_path(dirname):
    return os.path.join(dirname, 'multisample.xml')

# Returns elements from an XPath
def elts(root, expr):
    r = root.xpath(expr)
    if not r:
        raise KeyError
    return r

# Returns an element from an XPath
# This function raises an error if more than one element is matching.
def elt(root, expr):
    [r] = root.xpath(expr)
    return r

def convert_file(src, dst):
    status = subprocess.call(["ffmpeg", "-i", src, dst])
    if status != 0:
        raise RuntimeError("Could not convert")

def renoise_parse_sample_name(str):
    name, velocity, note = name.split(str)

def convert_xml(input, output):
    with open(input) as f:
        renoise = etree.parse(f)

    bitwig = etree.Element('multisample')
    layer = etree.SubElement(bitwig, 'layer')
    for sample in elts(renoise, '//Sample'):
        sample = etree.SubElement(layer, 'sample')
        sample.file =
        sample.gain = "0.000"
        sample.sample_start = "0.000"
        sample.sample_stop = elt(sample, "./LoopEnd/text()")
        sample.tune = "0.0"
        key = etree.SubElement(sample, "key")
        key.text = ......
        #velocity
        #loop mode
        


    with open(output, 'w') as f:
        f.write(etree.tostring(bitwig, pretty_print=True))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert from Renoise to Bitwig')
    parser.add_argument('--input', help='input dir')
    parser.add_argument('--output', help='output dir')

    args = parser.parse_args()

    convert_xml(renoise_manifest_path(args.input),
            bitwig_manifest_path(args.output))
