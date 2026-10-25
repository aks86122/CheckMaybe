// Static server that applies Cloudflare-style _headers (simple /* and /dir/* rules)
const http=require('http'),fs=require('fs'),path=require('path');const root=process.argv[2];
const rules=[];let cur=null;for(const l of fs.readFileSync(path.join(root,'_headers'),'utf8').split('\n')){if(!l.trim())continue;if(!/^\s/.test(l)){cur={pat:l.trim(),h:{}};rules.push(cur);}else{const i=l.indexOf(':');cur.h[l.slice(0,i).trim()]=l.slice(i+1).trim();}}
const T={'.html':'text/html','.js':'text/javascript','.css':'text/css','.json':'application/json','.png':'image/png'};
http.createServer((q,r)=>{let u=decodeURIComponent(q.url.split('?')[0]);if(u.endsWith('/'))u+='index.html';const f=path.join(root,u);
 if(!fs.existsSync(f)){r.writeHead(404);return r.end();}const h={'Content-Type':T[path.extname(f)]||'application/octet-stream'};
 for(const ru of rules){const p=ru.pat.replace(/\*$/,'');if(u.startsWith(p))Object.assign(h,ru.h);}r.writeHead(200,h);fs.createReadStream(f).pipe(r);}).listen(+process.argv[3]);
