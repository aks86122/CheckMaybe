/**
 * Holiday Hidden Cost Tracker: one-time polish for the Google Sheets master copy.
 *
 * Run this ONCE on your own master copy before sharing the template link. Buyers never run it.
 *   1. Upload Holiday-Hidden-Cost-Tracker.xlsx to Google Drive, open it, then File > Save as Google Sheets.
 *   2. In the new Google Sheet: Extensions > Apps Script. Delete the sample code, paste this whole file, save.
 *   3. Pick polishTemplate in the function list at the top and press Run. Allow access when asked (your own file only).
 *   4. Delete the code again and save. Everything it added stays in the file.
 *
 * What it does:
 *   - English (United States) locale and US Eastern time, so dates read "Dec 27" for every buyer.
 *   - Yes/No columns become real checkboxes (Free Trials "Cancelled?", Holiday Payments "1st paid at checkout?").
 *   - Filter bars (slicers) above the Gift List, Holiday Payments and Free Trials tables.
 *   - Rebuilds the two Dashboard charts as native dark Google charts.
 *   - Soft-protects the calculated cells (a warning, not a lock).
 * Safe to run again: it removes what it added before re-adding it.
 */
const C = {
  bg: '#101A14', panel: '#17251D', text: '#F3EFE4', muted: '#A7B2A3', line: '#2F4838',
  gold: '#E0B05A', berry: '#E2687B', berryDark: '#A8384B', green: '#74D39A', teal: '#5CC8B8', ice: '#9CC9F0', grey: '#8A948A'
};

function polishTemplate() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const gl = ss.getSheetByName('Gift List');
  const hp = ss.getSheetByName('Holiday Payments');
  const ft = ss.getSheetByName('Free Trials');
  const db = ss.getSheetByName('Dashboard');
  const cd = ss.getSheetByName('Chart Data');
  if (!gl || !hp || !ft || !db || !cd) {
    throw new Error('Tabs not found. Run this inside the Holiday Hidden Cost Tracker file, after File > Save as Google Sheets.');
  }
  const report = [];
  ss.setSpreadsheetLocale('en_US');
  ss.setSpreadsheetTimeZone('America/New_York');
  report.push('English (US) locale');
  report.push(addCheckboxes_(ft, 'G6:G25'));
  report.push(addCheckboxes_(hp, 'I6:I25'));
  report.push(addSlicers_(gl, 'B5:K55', [[2, 'Relationship'], [6, 'Paid with'], [7, 'Status'], [10, 'Payment plan']]));
  report.push(addSlicers_(hp, 'B5:Q25', [[2, 'Plan type'], [16, 'Flag']]));
  report.push(addSlicers_(ft, 'B5:L25', [[6, 'Cancelled?'], [11, 'Alert']]));
  report.push(rebuildCharts_(db, cd));
  report.push(protectFormulas_(ss));
  ss.setActiveSheet(db);
  Logger.log(report.join('\n'));
  ss.toast(report.join(' · '), 'Holiday tracker polished', 15);
}

function addCheckboxes_(sh, a1) {
  const rng = sh.getRange(a1);
  const vals = rng.getValues().map(row => row.map(v => (String(v).trim().toLowerCase() === 'yes' || v === true) ? 'Yes' : 'No'));
  rng.setValues(vals);
  rng.insertCheckboxes('Yes', 'No');
  rng.setHorizontalAlignment('center');
  return sh.getName() + ': checkboxes';
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
    .setOption('fontName', 'Arial')
    .setOption('width', w)
    .setOption('height', h);
}

function rebuildCharts_(db, cd) {
  db.getCharts().forEach(c => db.removeChart(c));
  const W = 490;

  const months = darkBase_(db.newChart().setChartType(Charts.ChartType.COLUMN), W, 265)
    .addRange(cd.getRange('B4:C9')).setNumHeaders(1)
    .setOption('colors', [C.berry])
    .setOption('legend', { position: 'none' })
    .setOption('bar', { groupWidth: '60%' })
    .setOption('vAxis', { format: '$#,##0', textStyle: { color: C.muted, fontSize: 9 }, gridlines: { color: C.line }, minorGridlines: { count: 0 }, baselineColor: C.line })
    .setOption('hAxis', { textStyle: { color: C.muted, fontSize: 9 } })
    .setPosition(14, 6, 0, 0)
    .build();
  db.insertChart(months);

  const paid = darkBase_(db.newChart().setChartType(Charts.ChartType.PIE), W, 265)
    .addRange(cd.getRange('B11:C18')).setNumHeaders(1)
    .setOption('pieHole', 0.58)
    .setOption('colors', [C.green, C.ice, C.gold, C.berry, C.berryDark, C.teal, C.grey])
    .setOption('pieSliceBorderColor', C.panel)
    .setOption('pieSliceText', 'percentage')
    .setOption('sliceVisibilityThreshold', 0.04)
    .setOption('pieSliceTextStyle', { color: C.bg, fontSize: 10, bold: true })
    .setPosition(30, 6, 0, 0)
    .build();
  db.insertChart(paid);
  return '2 dark charts';
}

function protectFormulas_(ss) {
  ss.getProtections(SpreadsheetApp.ProtectionType.RANGE)
    .filter(p => p.getDescription().indexOf('HHCT:') === 0)
    .forEach(p => p.remove());
  const areas = [
    ['Gift List', 'J6:L55'], ['Gift List', 'B3:K3'],
    ['Holiday Payments', 'K6:W25'], ['Holiday Payments', 'R5:V5'], ['Holiday Payments', 'B3:Q3'],
    ['Free Trials', 'H6:M25'], ['Free Trials', 'B3:L3'],
    ['Dashboard', 'B2:I60'],
    ['Chart Data', 'A1:G40']
  ];
  areas.forEach(([name, a1]) => {
    ss.getSheetByName(name).getRange(a1).protect()
      .setDescription('HHCT: calculated cells. Editing them breaks the formulas.')
      .setWarningOnly(true);
  });
  return 'formulas soft-protected';
}
