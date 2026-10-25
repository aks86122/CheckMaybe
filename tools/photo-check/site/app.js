const TOOLKIT = "https://checkmaybe.gumroad.com/l/kzhzh?utm_source=photocheck&utm_medium=tool&utm_campaign=v01";
const MAX = 20 * 1024 * 1024;
const EDITORS = [["Photoshop","Photoshop"],["PhotoDirector","PhotoDirector"],["PowerDirector","PowerDirector"],["YouCam","YouCam"],["BeautyPlus","BeautyPlus"],["B612","B612"],["PhotoRoom","PhotoRoom"],["Adobe Express","Adobe Express"],["Illustrator","Illustrator"],["Paint.NET","Paint.NET"],["Microsoft Photos","Microsoft Photos"],["Windows Photo","Microsoft Photos"],["Krita","Krita"],["Procreate","Procreate"],["Pixlr","Pixlr"],["Polarr","Polarr"],["Picasa","Picasa"],["ACDSee","ACDSee"],["XnView","XnView"],["IrfanView","IrfanView"],["Luminar","Luminar"],["Capture One","Capture One"],["darktable","darktable"],["Lightroom","Lightroom"],["Canva","Canva"],["Snapseed","Snapseed"],["PicsArt","PicsArt"],["GIMP","GIMP"],["Affinity","Affinity"],["Pixelmator","Pixelmator"],["VSCO","VSCO"],["Meitu","Meitu"],["Fotor","Fotor"],["CapCut","CapCut"],["Photopea","Photopea"],["Picsart","PicsArt"],["Remini","Remini"],["Lensa","Lensa"],["Facetune","Facetune"],["Instagram","Instagram"]];
const AI_TOKENS = [["trainedAlgorithmicMedia","made with generative AI"],["compositeWithTrainedAlgorithmicMedia","edited with generative AI"],["algorithmicMedia","made by an algorithm"]];
const GENERATORS = ["Canva AI","Adobe Firefly","Firefly","DALL-E","DALL·E","ChatGPT","OpenAI","Midjourney","Imagen","Gemini","Stable Diffusion","Canva","Microsoft Designer","Bing Image Creator","Meta AI","Leonardo"];
const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const kb = n => n > 1048576 ? (n / 1048576).toFixed(1) + " MB" : Math.round(n / 1024) + " KB";

function sniff(bytes) {
  const h = Array.from(bytes.slice(0, 12)).map(b => b.toString(16).padStart(2, "0")).join("");
  if (h.startsWith("ffd8ff")) return "JPEG";
  if (h.startsWith("89504e47")) return "PNG";
  if (h.startsWith("52494646") && h.slice(16, 24) === "57454250") return "WebP";
  if (h.slice(8, 16) === "66747970") return "HEIC";
  return null;
}

function scan(bytes) {
  // latin1 view of the whole file: C2PA (JUMBF) labels, XMP and IPTC fields are stored as plain text
  let txt = ""; const step = 65536;
  for (let i = 0; i < bytes.length; i += step) txt += String.fromCharCode.apply(null, bytes.subarray(i, i + step));
  const c2pa = /jumb/.test(txt) && /c2pa/.test(txt);
  const ai = AI_TOKENS.filter(([t]) => new RegExp(t).test(txt)).map(([, d]) => d);
  const aiExact = ai.length && txt.includes("compositeWithTrainedAlgorithmicMedia") ? ["edited with generative AI"] : ai.filter(d => d !== "made by an algorithm" || !txt.includes("trainedAlgorithmicMedia"));
  const gens = GENERATORS.filter(g => txt.includes(g));
  let cg = null;
  const ci = txt.indexOf("claim_generator_info");
  if (ci >= 0) { // CBOR map: ..."name" then a text string
    const ni = txt.indexOf("name", ci);
    if (ni > 0 && ni - ci < 40) { let k = ni + 4, h = txt.charCodeAt(k), n = 0;
      if (h >= 0x60 && h <= 0x77) { n = h - 0x60; k += 1; } else if (h === 0x78) { n = txt.charCodeAt(k + 1); k += 2; }
      if (n > 1 && n < 100) cg = txt.substr(k, n); }
  }
  if (!cg) { const m = txt.match(/claim_generator[^A-Za-z0-9_]{0,8}([A-Za-z0-9 ._/()+-]{3,60})/); if (m) cg = m[1].split(/\s+c2pa|\s+digitalSourceType|\s+trained/)[0]; }
  const actions = [...new Set((txt.match(/c2pa\.(created|edited|converted|placed|opened|filtered|color_adjustments|cropped|resized|drawing)/g) || []))];
  const xmp = txt.includes("<x:xmpmeta");
  const gainmap = txt.includes("hdr-gain-map") || txt.includes("GainMap");
  const uniq = [...new Set(gens)].filter((g, i, a) => !a.some(o => o !== g && o.includes(g)));
  if (cg && /c2pa|contentauth/i.test(cg) && uniq.length) cg = uniq[0] + " (" + cg.trim() + ")";
  const accountIds = /\b(doc|user|brand)=[A-Za-z0-9_-]{6,}/.test(txt);
  const dst = [...new Set([...txt.matchAll(/digitalsourcetype\/([A-Za-z]+)/gi)].map(x => x[1]).filter(c => DST[c]))];
  const shotText = /<[^>]*Screenshot|Screenshot<|UserComment[^<]{0,40}Screenshot/i.test(txt) || /\x00Screenshot\x00?/.test(txt);
  return { c2pa, ai: [...new Set(aiExact)], gens: uniq, cg: cg ? cg.trim() : null, actions, xmp, gainmap, accountIds, dst, shotText };
}

// IPTC Digital Source Type vocabulary (cv.iptc.org/newscodes/digitalsourcetype)
const DST = {
  digitalCapture: ["a camera capture", "g"], computationalCapture: ["a phone camera capture with built-in processing", "g"],
  negativeFilm: ["a film scan", "g"], positiveFilm: ["a film scan", "g"], print: ["a scan of a print", "g"],
  humanEdits: ["edited by a person", "a"], minorHumanEdits: ["lightly edited by a person", "a"], compositeCapture: ["a composite of camera captures", "a"],
  algorithmicallyEnhanced: ["enhanced by software", "a"], dataDrivenMedia: ["made from data", "a"], digitalArt: ["digital art made by a person", "a"],
  virtualRecording: ["a recording of a virtual scene", "a"], screenCapture: ["a screenshot", "b"], algorithmicMedia: ["made by an algorithm (not trained AI)", "a"],
  compositeSynthetic: ["a composite that includes synthetic parts", "r"], trainedAlgorithmicMedia: ["made with generative AI", "r"],
  compositeWithTrainedAlgorithmicMedia: ["edited with generative AI", "r"],
};
const SOCIAL = { "1000x1500": "a Pinterest pin", "2000x3000": "a Pinterest pin", "1080x1350": "an Instagram post", "1080x1920": "a story or Reel cover", "1080x1080": "a square social post", "1200x630": "a link preview", "1200x628": "a link preview", "1080x566": "a landscape Instagram post", "1280x720": "a video thumbnail" };
const AI_DST = ["trainedAlgorithmicMedia", "compositeWithTrainedAlgorithmicMedia", "compositeSynthetic"];
const SCREENS = ["1080x2448","1080x2400","1080x2340","1080x2412","1080x2460","1080x1920","1440x3200","1440x3088","1170x2532","1179x2556","1284x2778","1290x2796","1125x2436","1242x2688","828x1792","750x1334","1920x1080","2560x1440","1366x768","1536x864","1440x900","2880x1800","3840x2160","1600x900","1280x720"];

let c2paLib = null;
function loadC2pa() {
  if (!c2paLib) c2paLib = import("https://cdn.jsdelivr.net/npm/@contentauth/c2pa-web@0.15.3/inline/+esm")
    .then(async mod => ({ mod, c2pa: await mod.createC2pa() }));
  return c2paLib;
}
const VCODE = {
  "assertion.dataHash.mismatch": "The image was changed after it was signed, so the record no longer matches the pixels.",
  "claimSignature.mismatch": "The signature doesn't match the record.",
  "signingCredential.invalid": "The signing certificate couldn't be validated (it may have expired).",
  "signingCredential.revoked": "The signing certificate was revoked.",
};
async function readC2pa(file, mime) {
  try {
    const { mod, c2pa } = await loadC2pa();
    const rd = await mod.Reader.fromBlob(c2pa, mime, file);
    if (!rd) return { none: true };
    const st = await rd.manifestStore(); await rd.free();
    const man = st.manifests[st.active_manifest] || {};
    const acts = (man.assertions || []).filter(a => /^c2pa\.actions/.test(a.label)).flatMap(a => (a.data && a.data.actions) || []);
    const name = x => x && (x.name || (typeof x === "string" ? x : null));
    const all = Object.values(st.manifests || {});
    return {
      issuer: man.signature_info && man.signature_info.issuer,
      signedAt: man.signature_info && man.signature_info.time,
      gen: (man.claim_generator_info || []).map(g => g.name).filter(n => n && !/^c2pa|make_test/i.test(n)),
      agents: [...new Set(acts.map(a => name(a.softwareAgent)).filter(Boolean))],
      actions: [...new Set(acts.map(a => a.action))],
      dst: [...new Set(acts.map(a => (a.digitalSourceType || "").split("/").pop()).filter(Boolean))],
      watermark: acts.some(a => /watermark/.test(a.action)),
      state: st.validation_state || null,
      problems: [...new Set((st.validation_status || []).map(v => v.code).filter(c => VCODE[c]))].map(c => VCODE[c]),
      tampered: (st.validation_status || []).some(v => /dataHash\.mismatch|claimSignature\.mismatch|hash.*mismatch/.test(v.code)),
      changed: (st.validation_status || []).some(v => /Hash\.mismatch|hash.*mismatch/i.test(v.code)),
      ingredients: all.reduce((n, mm) => n + ((mm.ingredients || []).length), 0),
      history: all.length,
    };
  } catch (e) { return { error: true }; }
}

function dims(file, url) {
  return new Promise(res => { const im = new Image(); im.onload = () => res([im.naturalWidth, im.naturalHeight]); im.onerror = () => res(null); im.src = url; });
}

async function check(file) {
  if (!file.size) return { error: file.name + " is empty." };
  if (file.size > MAX) return { error: file.name + " is " + kb(file.size) + ". The limit is 20 MB." };
  const bytes = new Uint8Array(await file.arrayBuffer());
  const type = sniff(bytes);
  if (!type) return { error: file.name + " doesn't look like a JPEG, PNG, WebP or HEIC image." };
  let meta = {};
  try { meta = (await exifr.parse(bytes, { tiff: true, exif: true, gps: true, xmp: true, iptc: true, icc: false, makerNote: true, userComment: true, mergeOutput: true, translateValues: true })) || {}; } catch (e) { meta = {}; }
  const url = type === "HEIC" ? null : URL.createObjectURL(file);
  const wh = url ? await dims(file, url) : (meta.ExifImageWidth ? [meta.ExifImageWidth, meta.ExifImageHeight] : null);
  const s = scan(bytes);
  const mime = { JPEG: "image/jpeg", PNG: "image/png", WebP: "image/webp", HEIC: "image/heic" }[type];
  const cr = s.c2pa ? await readC2pa(file, mime) : null;
  return { file, type, meta, url, wh, s, cr };
}

function judge(r) {
  const m = r.meta, s = r.s, cr = r.cr && !r.cr.error && !r.cr.none ? r.cr : null;
  const name = r.file.name || "";
  const camera = m.Make || m.Model ? [m.Make, m.Model].filter(Boolean).join(" ") : null;
  const taken = m.DateTimeOriginal || m.CreateDate || null;
  const modified = m.ModifyDate || null;
  const sw = [m.Software, m.CreatorTool, m.HistorySoftwareAgent].filter(Boolean).map(x => String(x).replace(/\b(doc|user|brand)=[A-Za-z0-9_-]+/g, "$1=(hidden)"));
  const editors = [...new Set(sw.flatMap(x => EDITORS.filter(([k]) => x.toLowerCase().includes(k.toLowerCase())).map(([, n]) => n)))];
  const firmware = sw.length && !editors.length && (m.Make || m.Model) ? sw[0] : null;
  const otherApp = sw.length && !editors.length && !firmware ? sw[0] : null;
  const gps = m.latitude != null || m.GPSLatitude != null;
  const exposure = m.ExposureTime ? (m.ExposureTime < 1 ? "1/" + Math.round(1 / m.ExposureTime) : m.ExposureTime) + " s" : null;

  // Source type: C2PA actions first, then IPTC/XMP fields
  const dst = [...new Set([...(cr ? cr.dst : []), ...s.dst])].filter(c => DST[c]);
  const aiCodes = dst.filter(c => AI_DST.includes(c));
  const aiMark = aiCodes.length > 0 || (!cr && s.ai.length > 0);
  const aiWords = aiCodes.length ? aiCodes.map(c => DST[c][0]) : s.ai;
  const hasCreds = s.c2pa;
  const tools = [...new Set([...(cr ? [...cr.agents, ...cr.gen] : []), ...s.gens])].filter((g, i, a) => !a.some(o => o !== g && o.toLowerCase().includes(g.toLowerCase())));

  // Consistency checks on camera data
  const exifWH = m.ExifImageWidth && m.ExifImageHeight ? [m.ExifImageWidth, m.ExifImageHeight] : null;
  const resized = exifWH && r.wh && !((exifWH[0] === r.wh[0] && exifWH[1] === r.wh[1]) || (exifWH[0] === r.wh[1] && exifWH[1] === r.wh[0]));
  const gapMin = taken instanceof Date && modified instanceof Date ? Math.round((modified - taken) / 60000) : null;
  const resaved = gapMin != null && gapMin > 2;
  const noMakerNote = camera && !m.makerNote && !m.MakerNote;
  const screenSize = r.wh && (SCREENS.includes(r.wh[0] + "x" + r.wh[1]) || SCREENS.includes(r.wh[1] + "x" + r.wh[0]));
  const shotName = /^(screenshot|screen shot|螢幕|截圖|截屏|スクリーンショット)/i.test(name);
  const screenshot = dst.includes("screenCapture") || s.shotText || shotName || (/Screenshot/i.test(String(m.UserComment || "")));
  const stripped = !camera && !taken && !hasCreds && !aiMark && !editors.length;
  const sq = r.wh && r.wh[0] === r.wh[1] && [1080, 1440, 540, 640, 720, 1200].includes(r.wh[0]);
  const uuidName = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\.(jpe?g|png|webp)$/i.test(name);
  const chatName = /^\d{13}\.(jpe?g|png|webp)$/i.test(name) || /_\d{3}\.(jpe?g|png)$/i.test(name);
  const etsyName = /^il_(\d+x\w+|fullxfull)\.\d+_[a-z0-9]+\.(jpe?g|png|webp)$/i.test(name);
  const socialKind = r.wh ? SOCIAL[r.wh[0] + "x" + r.wh[1]] : null;
  const graphic = stripped && !screenshot && !etsyName && !chatName && socialKind && (r.type === "PNG" || r.wh[0] !== r.wh[1]);

  let level, title, text;
  if (etsyName && stripped) { level = "b"; title = "Saved from an Etsy listing";
    text = "Etsy re-saves every listing photo and removes camera data and AI markers, so a downloaded listing image can't show how it was made. Read the listing description for an AI disclosure, look for buyer photos in the reviews, or ask the seller for an unedited photo."; }
  else if (graphic) { level = "b"; title = "Looks like a designed graphic, not a photo";
    text = "No camera data, and the size matches " + socialKind + ". Graphics made in design apps or with code often mix photos, text and AI art, and the file can't show which. If any part was made with AI, say so yourself."; }
  else if (aiMark) { level = "r"; title = "This file says AI was used";
    text = "It carries a marker that platforms are known to read (" + aiWords.join(", ") + (tools.length ? ", by " + tools.join(", ") : "") + "). Instagram and Facebook may show an AI label, and Etsy expects you to disclose AI use in the listing."; }
  else if (screenshot) { level = "b"; title = "This looks like a screenshot";
    text = "A screenshot isn't a photo of your item. If it shows someone else's post, product or photo, you may not have the rights to use it in a listing."; }
  else if (hasCreds && cr && cr.tampered) { level = "r"; title = cr.changed ? "This file was changed after it was signed" : "Its Content Credentials signature is broken";
    text = (cr.changed ? "It has a Content Credentials record, but the image no longer matches it." : "The record's signature doesn't match.") + " Platforms may treat the record as broken. Use the original file if you have it."; }
  else if (hasCreds) { level = "a"; title = "This file has Content Credentials";
    text = "A C2PA record is attached" + (cr && cr.issuer ? ", signed by " + cr.issuer : "") + ". It doesn't say generative AI was used, but platforms read these records, so check what it says before you post."; }
  else if (editors.length) { level = "a"; title = "Edited in " + editors.join(", ");
    text = "Fine for most listing photos if the item still looks the way it really is. Exporting from an editor often removes AI markers too, so this can't show whether the image started as an AI image. For Etsy's required unedited photo, use a different, straight-from-camera shot."; }
  else if (camera && (resized || resaved)) { level = "a"; title = "A camera photo that was changed later";
    text = "The camera data is still there, but " + (resized ? "the image size no longer matches what the camera recorded" : "the file was saved again " + gapMin + " minutes after it was taken") + ". For Etsy's unedited photo, use the original from your camera roll."; }
  else if (camera) { level = "g"; title = "Looks like a straight-from-camera photo";
    text = "The file still has its camera data, its original size and no editing app name. That fits Etsy's unedited-photo rule, but file data can't prove a photo was never edited."; }
  else if (stripped) { level = "b"; title = "This file has almost no data left";
    text = (sq ? "Its size (" + r.wh[0] + " × " + r.wh[1] + ") is typical of photos saved from social media. " : "") + "Chat apps, social media, screenshots and many design and AI tools save images without this data, so the file can't show where the image came from. If it's your own photo, check the original from your camera roll."; }
  else { level = "b"; title = "Some data, no clear signal";
    text = "The file has some technical data but no camera details, editing app or AI marker."; }

  const facts = [
    ["Format", r.type + (r.wh ? " · " + r.wh[0] + " × " + r.wh[1] : "")],
    ["File size", kb(r.file.size)],
    ["Camera", camera || "Not found"],
    ["Taken", taken ? (taken instanceof Date ? taken.toLocaleString() : String(taken)) : "Not found"],
    ["Settings", [exposure, m.FNumber ? "f/" + m.FNumber : null, m.ISO ? "ISO " + m.ISO : null].filter(Boolean).join(" · ") || "Not found"],
    ["Software", sw.length ? sw.join(" · ") : "Not found"],
  ];
  if (exifWH && resized) facts.splice(1, 0, ["Size the camera recorded", exifWH[0] + " × " + exifWH[1]]);
  if (dst.length) facts.push(["Source type", dst.map(c => DST[c][0]).join(" · ")]);

  const sigs = [];
  sigs.push(aiMark ? ["r", "AI marker found", (aiCodes.length ? "Source type: " : "Marker: ") + aiWords.join(", ") + "."] : ["g", "No AI marker found", "None of the standard AI fields are present. This doesn't prove the image isn't AI-made."]);
  if (hasCreds) {
    if (cr) {
      let d = (cr.issuer ? "Signed by " + cr.issuer + " (name on the certificate; not checked against a trust list). " : "")
        + (cr.actions.length ? "Steps recorded: " + cr.actions.map(a => a.replace("c2pa.", "")).join(", ") + ". " : "")
        + (cr.ingredients ? "Made from " + cr.ingredients + " earlier file" + (cr.ingredients > 1 ? "s" : "") + ". " : "");
      sigs.push([cr.tampered ? "r" : "a", cr.tampered ? (cr.changed ? "Changed after signing" : "Signature broken") : cr.problems.length ? "Content Credentials: certificate issue" : "Content Credentials intact", d + (cr.problems.length ? cr.problems.join(" ") : "The signature matches the file.")]);
      if (cr.watermark) sigs.push(["a", "Invisible watermark recorded", "The record says a watermark was added to the pixels. It can survive screenshots and re-saves."]);
    } else {
      sigs.push(["a", "Content Credentials (C2PA)", (s.cg ? "Written by " + s.cg + ". " : "") + (r.cr && r.cr.error ? "The full check couldn't run in this browser, so the signature wasn't verified." : "")]);
    }
  } else sigs.push(["b", "No Content Credentials", "No C2PA record in the file."]);
  if (tools.length) sigs.push(["a", "Tools named in the file", tools.join(", ")]);
  sigs.push(editors.length ? ["a", "Editing app named", editors.join(", ")] : otherApp ? ["a", "App named", "The file was last saved by “" + otherApp + "”. There is no camera data, so this is not straight from a camera."] : firmware ? ["g", "Camera software only", "“" + firmware + "” looks like phone or camera firmware, not an editing app."] : ["b", "No software named", "The file doesn't say which app last saved it."]);
  if (resized) sigs.push(["a", "Size changed after capture", "The camera recorded " + exifWH[0] + " × " + exifWH[1] + "; the file is " + r.wh[0] + " × " + r.wh[1] + ". It was cropped or resized."]);
  if (resaved) sigs.push(["a", "Saved again later", "Last saved " + (gapMin >= 1440 ? Math.round(gapMin / 1440) + " days" : gapMin >= 60 ? Math.round(gapMin / 60) + " hours" : gapMin + " minutes") + " after it was taken."]);
  if (noMakerNote && !editors.length) sigs.push(["b", "Camera notes missing", "Phones and cameras usually store their own notes in the file. They're missing, so an app may have re-saved it."]);
  if (screenshot) sigs.push(["b", "Screenshot", shotName ? "The file name says it's a screenshot." : "The file is marked as a screen capture."]);
  else if (stripped && screenSize) sigs.push(["b", "Screen-sized image", "No camera data and the size matches a common phone or computer screen, so it may be a screenshot."]);
  if (s.gainmap && !camera) sigs.push(["g", "Phone HDR data", "An HDR gain map survived, a sign the image came from a phone camera."]);
  if (graphic) sigs.push(["b", "Social media size", r.wh[0] + " × " + r.wh[1] + " is the usual size for " + socialKind + "."]);
  if (etsyName && stripped) sigs.push(["b", "Etsy listing image", "The file name matches Etsy's image servers. Etsy keeps only a color profile; everything else is removed on upload."]);
  if (chatName && stripped) sigs.push(["b", "File name looks like a chat-app save", "Names like this usually come from saving an image out of a chat app such as LINE, which removes camera data. It may also be someone else's photo or screenshot."]);
  if (uuidName && stripped) sigs.push(["a", "File name looks like an app export", "Names like this usually come from design apps such as Canva, which save images without camera data. Treat it as an edited image."]);
  if (s.accountIds) sigs.push(["a", "Account IDs in the file", "The file lists a design-app document, user and brand ID (hidden here). Anyone who downloads the original can read them."]);
  if (gps) sigs.push(["r", "Location saved in the file", "Remove location before you post: anyone who downloads the original can read it."]);

  const todo = [];
  if (etsyName && stripped) todo.push("Check the listing description: Etsy requires sellers to disclose items made with AI.", "Look for review photos from other buyers; they show the real item.", "Ask the seller for an unedited photo of the actual item. Etsy now requires one on most listings.", "If the photos look misleading, use “Report this item to Etsy” and choose the misleading AI images option.");
  if (aiMark || tools.length) todo.push('Disclose AI use in your listing description (Etsy requires it). <a href="' + TOOLKIT + '" target="_blank" rel="noopener">Can I Use This?</a> p. 12');
  if (screenshot || chatName) todo.push('Only use images you made or have permission to use. <a href="https://checkmaybe.gumroad.com/l/baxojo?utm_source=photocheck&utm_medium=tool&utm_campaign=v01" target="_blank" rel="noopener">Can I Sell This?</a>');
  todo.push("For Etsy, keep at least one unedited photo of the actual item on a real background, unless your item type is an exception.");
  todo.push("Make sure every photo shows the real color, size, condition and flaws of what the buyer receives.");
  if (editors.includes("Canva") || tools.some(t => /canva/i.test(t))) todo.push('If you used Canva elements or AI tools, check that your license covers selling the result. <a href="https://checkmaybe.gumroad.com/l/baxojo?utm_source=photocheck&utm_medium=tool&utm_campaign=v01" target="_blank" rel="noopener">Can I Sell This?</a>');
  if (graphic) todo.push("If the graphic uses AI art or AI-edited photos, disclose it where you post it (for example Pinterest's “AI-modified” setting or your listing description).", "A designed graphic can't be Etsy's required unedited photo; use a real photo of the item for that.");
  else if (stripped && !screenshot) todo.push("If you made or edited this image with AI, disclose it yourself: the file no longer says so.", "For Etsy's unedited photo, upload the original from your camera roll, not an export from a design app.");
  todo.push("Keep the original file and the date you took it, in case a listing is questioned.");
  return { level, title, text, facts, sigs, todo, pixel: !(screenshot || graphic || aiMark) };
}

// Pixel check (opt-in): AI-image model run in the browser. The photo never leaves the device.
const PX = { base: "model/v1/", ort: "https://cdn.jsdelivr.net/npm/onnxruntime-web@1.20.1/dist/", line: 0.97, cache: "pixel-check-v1" };
function cub(x){x=Math.abs(x);const a=-0.5;return x<1?((a+2)*x-(a+3))*x*x+1:x<2?(((x-5)*x+8)*x-4)*a:0}
function coeffs(inS,outS){const sc=inS/outS,fs=Math.max(sc,1),sup=2*fs,W=[];
 for(let i=0;i<outS;i++){const ctr=(i+0.5)*sc;let x0=Math.max(0,Math.floor(ctr-sup+0.5)),x1=Math.min(inS,Math.floor(ctr+sup+0.5));const w=[];let t=0;
  for(let x=x0;x<x1;x++){const v=cub((x-ctr+0.5)/fs);w.push(v);t+=v}W.push([x0,w.map(v=>v/t)])}return W}
function resize(src,w,h,N){const H=coeffs(w,N),V=coeffs(h,N),tmp=new Float32Array(N*h*3),out=new Float32Array(N*N*3);
 for(let y=0;y<h;y++)for(let i=0;i<N;i++){const[x0,ws]=H[i];let r=0,g=0,b=0;for(let k=0;k<ws.length;k++){const p=(y*w+x0+k)*4;r+=src[p]*ws[k];g+=src[p+1]*ws[k];b+=src[p+2]*ws[k]}
  const q=(y*N+i)*3;tmp[q]=Math.min(255,Math.max(0,Math.round(r)));tmp[q+1]=Math.min(255,Math.max(0,Math.round(g)));tmp[q+2]=Math.min(255,Math.max(0,Math.round(b)))}
 for(let j=0;j<N;j++){const[y0,ws]=V[j];for(let i=0;i<N;i++){let r=0,g=0,b=0;for(let k=0;k<ws.length;k++){const q=((y0+k)*N+i)*3;r+=tmp[q]*ws[k];g+=tmp[q+1]*ws[k];b+=tmp[q+2]*ws[k]}
  const o=(j*N+i)*3;out[o]=Math.min(255,Math.max(0,Math.round(r)));out[o+1]=Math.min(255,Math.max(0,Math.round(g)));out[o+2]=Math.min(255,Math.max(0,Math.round(b)))}}return out}
let pxSession = null;
function loadScript(src) { return new Promise((ok, no) => { const t = document.createElement("script"); t.src = src; t.onload = ok; t.onerror = () => no(new Error("script")); document.head.append(t); }); }
async function sha256(buf) { const h = await crypto.subtle.digest("SHA-256", buf); return [...new Uint8Array(h)].map(b => b.toString(16).padStart(2, "0")).join(""); }
async function getPart(cache, url, part) {
  let res = cache ? await cache.match(url) : null;
  if (!res) { res = await fetch(url); if (!res.ok) throw new Error("download"); if (cache) { try { await cache.put(url, res.clone()); } catch (e) {} } }
  const buf = await res.arrayBuffer();
  if (buf.byteLength !== part.size || await sha256(buf) !== part.sha256) { if (cache) await cache.delete(url); throw new Error("corrupt"); }
  return buf;
}
function loadModel(progress) {
  return pxSession = pxSession || (async () => {
    if (typeof ort === "undefined") await loadScript(PX.ort + "ort.wasm.min.js");
    ort.env.wasm.wasmPaths = PX.ort; ort.env.wasm.numThreads = self.crossOriginIsolated ? Math.min(4, navigator.hardwareConcurrency || 1) : 1;
    const man = await (await fetch(PX.base + "manifest.json")).json();
    let cache = null; try { cache = await caches.open(PX.cache); } catch (e) {}
    const all = new Uint8Array(man.total); let at = 0;
    for (const part of man.parts) { all.set(new Uint8Array(await getPart(cache, PX.base + part.name, part)), at); at += part.size; progress(Math.round(at / man.total * 100)); }
    progress(null);
    return ort.InferenceSession.create(all, { executionProviders: ["wasm"] });
  })().catch(e => { pxSession = null; throw e; });
}
async function pixelScore(url, progress) {
  const s = await loadModel(progress);
  const im = new Image(); im.src = url; await im.decode();
  const k = Math.min(1, 8192 / Math.max(im.naturalWidth, im.naturalHeight)), w = Math.round(im.naturalWidth * k), h = Math.round(im.naturalHeight * k);
  const cv = document.createElement("canvas"); cv.width = w; cv.height = h; const g = cv.getContext("2d"); g.drawImage(im, 0, 0, w, h);
  const d = resize(g.getImageData(0, 0, w, h).data, w, h, 256), N = 65536, x = new Float32Array(3 * N), M = [.485, .456, .406], SD = [.229, .224, .225];
  for (let j = 0; j < N; j++) for (let c = 0; c < 3; c++) x[c * N + j] = (d[j * 3 + c] / 255 - M[c]) / SD[c];
  const out = await s.run({ pixel_values: new ort.Tensor("float32", x, [1, 3, 256, 256]) });
  return out.probs.data[0];
}
function pixelBlock(r, j, example) {
  const box = document.createElement("div"); box.className = "srch px";
  if (example || !r.url || !j.pixel) return box;
  box.innerHTML = '<div class="row"><strong>Pixel check (optional)</strong><button class="btn ghost" type="button">Run pixel check</button></div>' +
    '<p class="note">An AI-image model looks at the pixels on your device; the photo is not uploaded. First time: a 199 MB download that stays in your browser, then about 10 seconds on a computer or 30 to 40 seconds on a phone.</p>' +
    '<p class="note pxout" aria-live="polite"></p>';
  const btn = box.querySelector("button"), out = box.querySelector(".pxout");
  btn.addEventListener("click", async () => {
    btn.disabled = true; out.textContent = "Starting…";
    try {
      const sc = await pixelScore(r.url, p => { out.textContent = p == null ? "Preparing the model…" : "Downloading the model: " + p + "%"; });
      r.pixel = Math.round(sc * 1000) / 1000;
      out.innerHTML = sc >= PX.line ? '<span class="chip a">Strong AI-like patterns</span> The pixels look like many AI-made images. Pixel checks can be wrong, especially on edited or compressed photos, so treat this as a reason to ask, not proof.'
        : '<span class="chip b">No strong AI-like patterns</span> That does not prove the image is real: compression, edits and newer AI tools can hide the patterns.';
      btn.hidden = true;
    } catch (e) { out.textContent = e.message === "corrupt" ? "The download was damaged. Try again." : "The pixel check couldn't run in this browser (" + (e.message || "error") + ")."; btn.disabled = false; }
  });
  return box;
}

// Reverse image search links
const ENG = { tineye: u => "https://tineye.com/search?url=" + encodeURIComponent(u), lens: u => "https://lens.google.com/uploadbyurl?url=" + encodeURIComponent(u), bing: u => "https://www.bing.com/images/search?view=detailv2&iss=sbi&q=imgurl:" + encodeURIComponent(u) };
const HOME = { tineye: "https://tineye.com/", lens: "https://lens.google.com/", bing: "https://www.bing.com/visualsearch" };
$("#revurl").addEventListener("input", e => { const v = e.target.value.trim(); const ok = /^https?:\/\/\S+$/i.test(v);
  document.querySelectorAll("#revlinks a").forEach(a => { a.href = ok ? ENG[a.dataset.eng](v) : HOME[a.dataset.eng]; }); });

// Feedback: answers + the check's findings only (no image, file name, location or account IDs)
const REAL = [["camera", "A straight-from-camera photo"], ["edited", "An edited photo"], ["ai_made", "Made with AI"], ["ai_edited", "A photo edited with AI"], ["screenshot", "A screenshot"], ["not_mine", "Someone else's image"], ["design", "A design or mockup (not a photo)"], ["unsure", "Not sure"]];
// Feedback goes through a public Google Form (anonymous; the visitor presses Submit on Google's page)
const FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfg9uYwbop9UluT99vYxWx0rmEMF5z41XexQMlR6C49Fb5DYQ/viewform";
const FORM_IDS = { right: "entry.1031372084", actual: "entry.2118168332", tool: "entry.920764767", comment: "entry.1367118987", check: "entry.1662659418" };
const FORM_ACTUAL = { camera: "A straight-from-camera photo", edited: "An edited photo", ai_made: "Made with AI", ai_edited: "A photo edited with AI", screenshot: "A screenshot", not_mine: "Someone else\u2019s image", design: "A design or mockup (not a photo)", unsure: "Not sure" };
function formUrl(f) {
  const q = new URLSearchParams({ usp: "pp_url" });
  for (const k of Object.keys(FORM_IDS)) if (f[k]) q.set(FORM_IDS[k], f[k]);
  return FORM + "?" + q.toString();
}
function nameKind(n) { return /^il_(\d+x\w+|fullxfull)\./i.test(n) ? "etsy" : /^\d{13}\./.test(n) ? "chat13" : /_\d{3}\.(jpe?g|png)$/i.test(n) ? "chat_suffix" : /^[0-9a-f]{8}-[0-9a-f]{4}-/i.test(n) ? "uuid" : /^(screenshot|screen shot|螢幕|截圖)/i.test(n) ? "screenshot" : /^(IMG|PXL|DSC|P)_\d{8}/i.test(n) ? "camera_name" : "other"; }
function features(r, j) {
  const m = r.meta || {}, s = r.s || {}, cr = r.cr && !r.cr.error && !r.cr.none ? r.cr : null;
  return { verdict: j.title, level: j.level, signals: j.sigs.map(x => x[1]).slice(0, 14), type: r.type || null, w: r.wh ? r.wh[0] : null, h: r.wh ? r.wh[1] : null,
    sizeKB: r.file && r.file.size ? Math.round(r.file.size / 1024) : null, camera: !!(m.Make || m.Model), makerNote: !!(m.makerNote || m.MakerNote), c2pa: !!s.c2pa,
    c2paChecked: !!cr, issuer: cr && cr.issuer ? String(cr.issuer).slice(0, 80) : null, dst: [...new Set([...(cr ? cr.dst : []), ...(s.dst || [])])].slice(0, 6),
    tools: [...new Set([...(cr ? [...cr.agents, ...cr.gen] : []), ...(s.gens || [])])].slice(0, 6).map(t => String(t).slice(0, 60)), nameKind: nameKind(r.file.name || r.name || ""), pixel: r.pixel == null ? null : r.pixel };
}
function feedbackBlock(r, j, example) {
  const box = document.createElement("div"); box.className = "fb";
  if (example) { box.innerHTML = '<p class="note">Check your own photo to rate the result.</p>'; return box; }
  const id = "fb" + Math.random().toString(36).slice(2, 9);
  box.innerHTML = '<div class="row"><span>Was this result right?</span><button class="btn ghost" type="button" data-a="yes">Yes</button><button class="btn ghost" type="button" data-a="no">No</button></div>' +
    '<div class="more" hidden><div class="row"><label for="' + id + 's">What is it really?</label><select id="' + id + 's">' + REAL.map(([v, t]) => '<option value="' + v + '">' + t + '</option>').join("") + '</select>' +
    '<input id="' + id + 't" type="text" maxlength="60" placeholder="App or AI tool used (optional)" aria-label="App or AI tool used"></div>' +
    '<textarea id="' + id + 'c" maxlength="500" placeholder="Anything else we should know? (optional, no personal details)" aria-label="Comment"></textarea></div>' +
    '<div class="row send" hidden><a class="btn" data-a="send" href="' + FORM + '" target="_blank" rel="noopener">Send feedback</a></div>' +
    '<p class="note">Send opens a short Google Form with your answers and this check\'s findings (format, size, which markers were found) filled in. Nothing is sent until you press Submit there. Never the photo, its file name, location or account IDs. The CheckMaybe team reads what you send, so leave out names, contact details and anything private.</p><p class="note status" aria-live="polite"></p>';
  let correct = null; const more = box.querySelector(".more"), send = box.querySelector(".send"), status = box.querySelector(".status");
  // Keep the link's address current at all times: the claude.ai viewer may open a link with the address it had before the click handlers ran.
  const link = box.querySelector('[data-a="send"]');
  const update = () => { const check = Object.assign({ tool_version: "0.4" }, features(r, j));
    link.href = formUrl({ right: correct === null ? null : correct ? "Yes" : "No", actual: correct === false ? FORM_ACTUAL[box.querySelector("#" + id + "s").value] : null,
      tool: correct === false ? (box.querySelector("#" + id + "t").value || "").trim().slice(0, 60) : null, comment: correct === false ? (box.querySelector("#" + id + "c").value || "").trim().slice(0, 500) : null,
      check: JSON.stringify(check) }); };
  update();
  box.addEventListener("input", update); box.addEventListener("change", update);
  box.addEventListener("click", e => { const a = e.target.dataset && e.target.dataset.a; if (!a) return;
    if (a === "yes" || a === "no") { correct = a === "yes"; more.hidden = correct; send.hidden = false; box.querySelectorAll('[data-a="yes"],[data-a="no"]').forEach(b => b.setAttribute("aria-pressed", String(b.dataset.a === a))); update(); return; }
    if (a === "send") { update(); status.textContent = "The form opened in a new tab. Press Submit there to send it. Thanks!"; } });
  return box;
}

function searchBlock(r, example) {
  const box = document.createElement("div"); box.className = "srch";
  const etsy = /^il_(\d+x\w+|fullxfull)\./i.test(r.file.name || r.name || "");
  box.innerHTML = '<div class="row"><strong>Is this image used somewhere else?</strong></div>' +
    '<div class="row">' + (r.url && !example ? '<button class="btn" type="button" data-copy>Copy image</button>' : '') +
    '<a class="btn ghost" href="https://lens.google.com/" target="_blank" rel="noopener">Open Google Lens</a>' +
    '<a class="btn ghost" href="https://tineye.com/" target="_blank" rel="noopener">Open TinEye</a>' +
    '<a class="btn ghost" href="https://www.bing.com/visualsearch" target="_blank" rel="noopener">Open Bing</a></div>' +
    '<p class="note">' + (etsy ? "For a listing photo, pasting its image address in the box at the bottom of this page searches all three at once." :
      "Copy the image, open a search site and paste it (Ctrl+V or ⌘V), or drag the photo file onto the site. The photo goes to that site, not to us.") + '</p>' +
    '<p class="note cstatus" aria-live="polite"></p>';
  const btn = box.querySelector("[data-copy]");
  if (btn) btn.addEventListener("click", async () => {
    const st = box.querySelector(".cstatus");
    try {
      const img = box.closest(".sheet").querySelector("img.thumb"); const im = new Image(); im.src = img.src; await im.decode();
      const max = 2000, k = Math.min(1, max / Math.max(im.naturalWidth, im.naturalHeight));
      const cv = document.createElement("canvas"); cv.width = Math.round(im.naturalWidth * k); cv.height = Math.round(im.naturalHeight * k);
      cv.getContext("2d").drawImage(im, 0, 0, cv.width, cv.height);
      const blob = await new Promise(res => cv.toBlob(res, "image/png"));
      await navigator.clipboard.write([new ClipboardItem({ "image/png": blob })]);
      st.textContent = "Copied. Open a search site and paste it.";
    } catch (e) { st.textContent = "Copying images isn't allowed here. Open a search site and drag the photo file onto it instead."; }
  });
  return box;
}

function render(r, example) {
  const j = r.j || judge(r);
  const el = document.createElement("article"); el.className = "sheet";
  el.innerHTML =
    '<div class="sheet-head">' + (r.url ? '<img class="thumb" alt="" src="' + r.url + '">' : '<div class="thumb" aria-hidden="true"></div>') +
    '<div class="name">' + esc(r.name || r.file.name) + '</div>' + (example ? '<span class="tag example">Example result</span>' : '') + '</div>' +
    '<div class="verdict"><span class="chip ' + j.level + '">' + ({ g: "Lower concern", a: "Check first", r: "Platforms may label it", b: "Not enough data" }[j.level]) + '</span><h2>' + esc(j.title) + '</h2><p>' + esc(j.text) + '</p></div>' +
    '<div class="cols"><div class="col"><h3>In the file</h3><dl>' + j.facts.map(([k, v]) => '<div><dt>' + k + '</dt><dd>' + esc(v) + '</dd></div>').join("") + '</dl></div>' +
    '<div class="col"><h3>What platforms can read</h3>' + j.sigs.map(([c, t, d]) => '<div class="sig"><span class="chip ' + c + '">' + esc(t) + '</span><span>' + esc(d) + '</span></div>').join("") + '</div>' +
    '<div class="col"><h3>Still for you to check</h3><ul class="todo">' + j.todo.map(t => '<li>' + t + '</li>').join("") + '</ul></div></div>' +
    '<div class="foot"><button class="btn ghost" type="button">Copy report</button><small>Checked ' + new Date().toLocaleDateString() + ' · not legal advice</small></div>';
  const btn = el.querySelector("button");
  btn.addEventListener("click", async () => {
    const text = ["CheckMaybe photo check", (r.name || r.file.name), j.title, j.text, "", "In the file:", ...j.facts.map(([k, v]) => "- " + k + ": " + v), "", "What platforms can read:", ...j.sigs.map(([, t, d]) => "- " + t + ": " + d), "", "Still to check:", ...j.todo.map(t => "- " + t.replace(/<[^>]+>/g, "")), "", "Missing data doesn't prove a photo isn't AI-made or was never edited. Not legal advice."].join("\n");
    try { await navigator.clipboard.writeText(text); btn.textContent = "Copied"; }
    catch (e) { const ta = document.createElement("textarea"); ta.value = text; ta.style.cssText = "width:100%;height:200px"; el.querySelector(".foot").append(ta); ta.select(); btn.textContent = "Select and copy the text"; }
  });
  el.querySelector(".foot").before(pixelBlock(r, j, example), searchBlock(r, example));
  el.append(feedbackBlock(r, j, example));
  return el;
}

async function handle(files) {
  const err = $("#err"); err.hidden = true; const box = $("#results");
  box.querySelectorAll(".sheet").forEach(n => { const i = n.querySelector("img.thumb"); if (i && i.src.startsWith("blob:")) URL.revokeObjectURL(i.src); });
  box.innerHTML = ""; const errors = [];
  if (typeof exifr === "undefined") { err.textContent = "The checker couldn't load. Reload the page and try again."; err.hidden = false; return; }
  for (const f of files) { const r = await check(f); if (r.error) errors.push(r.error); else box.append(render(r)); }
  if (errors.length) { err.textContent = errors.join(" "); err.hidden = false; }
}

const drop = $("#drop");
$("#pick").addEventListener("change", e => handle([...e.target.files]));
["dragenter", "dragover"].forEach(t => drop.addEventListener(t, e => { e.preventDefault(); drop.classList.add("over"); }));
["dragleave", "drop"].forEach(t => drop.addEventListener(t, e => { e.preventDefault(); drop.classList.remove("over"); }));
drop.addEventListener("drop", e => handle([...e.dataTransfer.files]));

// Example result so the page shows what it does before a photo is chosen (made-up values)
$("#results").append(render({ name: "example-phone-photo.jpg", file: { size: 2263007 }, j: {
  level: "g", title: "Looks like a straight-from-camera photo",
  text: "The file still has its camera data and no editing app name. That fits Etsy's unedited-photo rule, but file data can't prove a photo was never edited.",
  facts: [["Format", "JPEG · 4096 × 2304"], ["File size", "2.2 MB"], ["Camera", "Example phone model"], ["Taken", "2026-10-24 23:17"], ["Settings", "1/60 s · f/1.9 · ISO 75"], ["Software", "Phone firmware build"]],
  sigs: [["g", "No AI marker found", "None of the standard AI fields are present. This doesn't prove the image isn't AI-made."], ["b", "No Content Credentials", "No C2PA record in the file."], ["g", "Camera software only", "The software field looks like phone firmware, not an editing app."]],
  todo: ["For Etsy, keep at least one unedited photo of the actual item on a real background, unless your item type is an exception.", "Make sure every photo shows the real color, size, condition and flaws of what the buyer receives.", "Keep the original file and the date you took it, in case a listing is questioned."] } }, true));
