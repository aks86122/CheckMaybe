/**
 * Hidden Cost Tracker: one-time polish for the Google Sheets master copy.
 *
 * Run this ONCE on your own master copy before sharing the template link. Buyers never run it.
 *   1. Upload hidden-cost-tracker-prototype.xlsx to Google Drive, open it, then File > Save as Google Sheets.
 *   2. In the new Google Sheet: Extensions > Apps Script. Delete the sample code, paste this whole file, save.
 *   3. Pick polishTemplate in the function list at the top and press Run. Allow access when asked (your own file only).
 *
 * What it does:
 *   - Yes/No columns on Subscriptions become real checkboxes (formulas keep working: ticked = "Yes").
 *   - Filter bars (slicers) above the Subscriptions and Debts tables.
 *   - Rebuilds the three Dashboard charts as native dark Google charts.
 *   - Sets the file to English (United States) and US Eastern time, so dates read "Oct 2" instead of the
 *     uploader's local language, and every buyer's copy starts in English.
 *   - Soft-protects the calculated columns (a warning, not a lock) so buyers don't overwrite formulas by accident.
 * Safe to run again: it removes what it added before re-adding it.
 */
const C = {
  bg: '#15171F', panel: '#1E2130', input: '#262A3D', text: '#EDEBF5', muted: '#9A98AE', line: '#33384F',
  orange: '#F08A4B', blue: '#8AB4FF', red: '#FF6B6B', amber: '#F2B544', green: '#5FD38D', purple: '#B18CFF', pink: '#F06BC8'
};

function polishTemplate() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const su = ss.getSheetByName('Subscriptions');
  const de = ss.getSheetByName('Debts & Installments');
  const db = ss.getSheetByName('Dashboard');
  const cd = ss.getSheetByName('Chart Data');
  if (!su || !de || !db || !cd) {
    throw new Error('Tabs not found. Run this inside the Hidden Cost Tracker file, after File > Save as Google Sheets.');
  }
  const report = [];
  ss.setSpreadsheetLocale('en_US');
  ss.setSpreadsheetTimeZone('America/New_York');
  report.push('English (US) locale');
  report.push(addCheckboxes_(su));
  report.push(addSlicers_(su, 'B5:R35', [[3, 'Category'], [5, 'Billing'], [9, 'Cancel it?'], [18, 'Alert']]));
  report.push(addSlicers_(de, 'B5:R25', [[3, 'Type'], [18, 'Flag']]));
  report.push(rebuildCharts_(db, cd));
  report.push(protectFormulas_(ss));
  ss.setActiveSheet(db);
  Logger.log(report.join('\n'));
  ss.toast(report.join(' · '), 'Hidden Cost Tracker polished', 15);
}

function addCheckboxes_(sh) {
  const rng = sh.getRange('H6:J35');
  const vals = rng.getValues().map(row => row.map(v => (String(v).trim().toLowerCase() === 'yes' || v === true) ? 'Yes' : 'No'));
  rng.setValues(vals);
  rng.insertCheckboxes('Yes', 'No');
  rng.setHorizontalAlignment('center');
  return 'checkboxes added';
}

function addSlicers_(sh, a1, cols) {
  sh.getSlicers().forEach(s => s.remove());
  const range = sh.getRange(a1);
  const make = () => cols.forEach(([pos, title], i) => {
    const s = sh.insertSlicer(range, 4, 2, 4 + i * 190, 4);
    s.setColumnFilterCriteria(pos, SpreadsheetApp.newFilterCriteria().build());
    s.setTitle(title);
    s.setBackgroundColor(C.panel);
    s.setTitleTextStyle(SpreadsheetApp.newTextStyle().setForegroundColor(C.text).setBold(true).setFontSize(9).build());
  });
  try {
    make();
  } catch (e) {
    // A sheet-wide filter can block slicers on some accounts: drop it and retry (slicers do the filtering).
    const f = sh.getFilter();
    if (f) f.remove();
    sh.getSlicers().forEach(s => s.remove());
    make();
  }
  return sh.getName() + ': ' + cols.length + ' filter bars';
}

function darkBase_(builder, w, h) {
  return builder
    .setHiddenDimensionStrategy(Charts.ChartHiddenDimensionStrategy.SHOW_BOTH)
    .setOption('backgroundColor', C.panel)
    .setOption('chartArea', { backgroundColor: C.panel })
    .setOption('legend', { position: 'right', textStyle: { color: C.text, fontSize: 10 } })
    .setOption('titleTextStyle', { color: C.text })
    .setOption('fontName', 'Arial')
    .setOption('width', w)
    .setOption('height', h);
}

function axes_(builder, valueFormat, valueAxis) {
  const val = { format: valueFormat, textStyle: { color: C.muted, fontSize: 9 }, gridlines: { color: C.line }, minorGridlines: { count: 0 }, baselineColor: C.line };
  const cat = { textStyle: { color: C.muted, fontSize: 9 }, gridlines: { color: 'transparent' }, baselineColor: C.line };
  return valueAxis === 'h' ? builder.setOption('hAxis', val).setOption('vAxis', cat) : builder.setOption('vAxis', val).setOption('hAxis', cat);
}

function rebuildCharts_(db, cd) {
  db.getCharts().forEach(c => db.removeChart(c));
  const W = 490, H = 250;

  const donut = darkBase_(db.newChart().setChartType(Charts.ChartType.PIE), W, H)
    .addRange(cd.getRange('B4:C8')).setNumHeaders(1)
    .setOption('pieHole', 0.58)
    .setOption('colors', [C.red, C.amber, C.purple, C.green])
    .setOption('pieSliceBorderColor', C.panel)
    .setOption('pieSliceText', 'percentage')
    .setOption('pieSliceTextStyle', { color: C.bg, fontSize: 10, bold: true })
    .setPosition(14, 6, 0, 0)
    .build();
  db.insertChart(donut);

  const spend = axes_(darkBase_(db.newChart().setChartType(Charts.ChartType.COLUMN), W, 280), '$#,##0', 'v')
    .addRange(cd.getRange('B11:D20')).setNumHeaders(1)
    .setOption('colors', [C.purple, C.green])
    .setOption('legend', { position: 'top', alignment: 'end', textStyle: { color: C.text, fontSize: 10 } })
    .setOption('bar', { groupWidth: '70%' })
    .setOption('hAxis', { textStyle: { color: C.muted, fontSize: 9 }, slantedText: true, slantedTextAngle: 35 })
    .setPosition(28, 6, 0, 0)
    .build();
  db.insertChart(spend);

  const apr = axes_(darkBase_(db.newChart().setChartType(Charts.ChartType.BAR), W, 280), '#%', 'h')
    .addRange(cd.getRange('B23:C31')).setNumHeaders(1)
    .setOption('colors', [C.orange])
    .setOption('legend', { position: 'none' })
    .setOption('bar', { groupWidth: '65%' })
    .setPosition(45, 6, 0, 0)
    .build();
  db.insertChart(apr);
  return '3 dark charts';
}

function protectFormulas_(ss) {
  ss.getProtections(SpreadsheetApp.ProtectionType.RANGE)
    .filter(p => p.getDescription().indexOf('HCT:') === 0)
    .forEach(p => p.remove());
  const areas = [
    ['Subscriptions', 'L6:U35'], ['Subscriptions', 'B3:R3'],
    ['Debts & Installments', 'J6:S25'], ['Debts & Installments', 'B3:R3'],
    ['Dashboard', 'B2:I26'], ['Dashboard', 'B27:H27'], ['Dashboard', 'B28:I64'],
    ['Chart Data', 'A1:G34']
  ];
  areas.forEach(([name, a1]) => {
    ss.getSheetByName(name).getRange(a1).protect()
      .setDescription('HCT: calculated cells. Editing them breaks the formulas.')
      .setWarningOnly(true);
  });
  return 'formulas soft-protected';
}
