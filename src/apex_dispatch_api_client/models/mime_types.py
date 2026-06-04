from enum import Enum


class MimeTypes(str, Enum):
    APPLICATIONGEOJSON = "application/geo+json"
    APPLICATIONGEOJSON_SEQ = "application/geo+json-seq"
    APPLICATIONGEOPACKAGESQLITE3 = "application/geopackage+sqlite3"
    APPLICATIONJSON = "application/json"
    APPLICATIONNDJSON = "application/ndjson"
    APPLICATIONOCTET_STREAM = "application/octet-stream"
    APPLICATIONPDF = "application/pdf"
    APPLICATIONSCHEMAJSON = "application/schema+json"
    APPLICATIONVND_APACHE_PARQUET = "application/vnd.apache.parquet"
    APPLICATIONVND_GOOGLE_EARTH_KMLXML = "application/vnd.google-earth.kml+xml"
    APPLICATIONVND_GOOGLE_EARTH_KMZ = "application/vnd.google-earth.kmz"
    APPLICATIONVND_MAPBOX_VECTOR_TILE = "application/vnd.mapbox-vector-tile"
    APPLICATIONVND_OAI_OPENAPIJSONVERSION3_0 = (
        "application/vnd.oai.openapi+json;version=3.0"
    )
    APPLICATIONVND_OAI_OPENAPIVERSION3_0 = "application/vnd.oai.openapi;version=3.0"
    APPLICATIONXML = "application/xml"
    APPLICATIONX_HDF = "application/x-hdf"
    APPLICATIONX_HDF5 = "application/x-hdf5"
    APPLICATIONX_PROTOBUF = "application/x-protobuf"
    IMAGEJP2 = "image/jp2"
    IMAGEJPEG = "image/jpeg"
    IMAGEPNG = "image/png"
    IMAGETIFF_APPLICATIONGEOTIFF = "image/tiff; application=geotiff"
    IMAGETIFF_APPLICATIONGEOTIFF_PROFILECLOUD_OPTIMIZED = (
        "image/tiff; application=geotiff; profile=cloud-optimized"
    )
    TEXTCSV = "text/csv"
    TEXTHTML = "text/html"
    TEXTPLAIN = "text/plain"

    def __str__(self) -> str:
        return str(self.value)
