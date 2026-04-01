from pyrevit import revit, DB, forms
from pyrevit.forms import WPFWindow
import os
import time

# Create UI class
class ExportWindow(WPFWindow):
    def __init__(self):
        # Load the XAML window
        WPFWindow.__init__(self, 'ui.xaml')

        # Get current document
        self.doc = revit.doc

        # Collect all sheets
        all_sheets = DB.FilteredElementCollector(self.doc).OfClass(DB.ViewSheet).ToElements()
        self.sheets = {}
        for sheet in all_sheets:
            self.sheets[sheet.Name] = sheet

        # Fill ComboBox
        self.SheetComboBox.ItemsSource = list(self.sheets.keys())

        # Bind Export button
        self.ExportBtn.Click += self.export_sheet

    # Export selected sheet
    def export_sheet(self, sender, args):
        selected_sheet_name = self.SheetComboBox.SelectedItem
        if not selected_sheet_name:
            forms.alert("Please select a sheet to export.")
            return

        sheet = self.sheets[selected_sheet_name]

        # Choose folder via dialog
        folder = forms.pick_folder('Select export folder')
        if not folder:
            forms.alert('Export canceled: no folder selected.')
            return

        if not os.path.exists(folder):
            os.makedirs(folder)

        options = DB.PDFExportOptions()
        options.Combine = False

        start_time = time.time()
        #forms.alert('Exporting "{} - {}" to "{}"...'.format(sheet.SheetNumber, sheet.Name, folder))
        #form alerts exporting format in the folder in the sheetnumber, sheetname, and the format

        try:
            self.doc.Export(folder, [sheet.Id], options)
            elapsed = time.time() - start_time
            forms.alert('Export successful.\nSheet: {} - {}\nFolder: {}\nTime: {:.2f}s'.format(sheet.SheetNumber, sheet.Name, folder, elapsed))
        except Exception as e:
            forms.alert('Export failed: {}'.format(str(e)))

# Show the window
ExportWindow().ShowDialog()

#.................end..................