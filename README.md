# Line Extractor for OCR Detection
Detection and Extraction of individual line(s) of text from a pdf document.

## Functionality
- Detection of individual lines from a Text Document using OpenCV
- Extraction of the Exact Coordinates (Pixel Values of the Bounding Boxes) and saving them as a JSON file.

## Dependencies
- **Poppler** \& **pdf2image** (For Converting 'pdf' files to 'jpeg')
- **OpenCV** (For detecting Lines from an Image file) 
- **NumPy** (For some mathematical requirements)

## Output
- Pdf to Image: Location [ _/data/jpeg/page\_*.jpeg_ ]
- Files (Pages) with the detected lines: Location [ _/extracted/page\_*/b\_box\_page\_\*.jpeg_ ]
- Bounding Boxes: Location [ _/extracted/page_no/boxes/box*.jpeg_ ]
- Coordinates for the Bounding Box(s): [ _/extracted/page\_*.jpeg_ ]

