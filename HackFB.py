import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))