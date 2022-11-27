// 자바스크립트 백엔드


// 브라우저 환경의 전역객체: window 객체
// 노드 환경의 전역객체: global 객체
// 웹 워커 환경의 전역객체: self 객체

// path 모듈
let path = require('path');
let directories = ['nodejsProjects', 'basicProject', 'nodejs', 'node1.js'];
let dirStr1 = directories.join(path.sep);
console.log(dirStr1);
let filepath = path.join('nodejsProjects/basicProject/nodejs', 'nodejs.js');
console.log(filepath);

let dirname = path.dirname(filepath); // 폴더명
console.log('dirname : ' + dirname);
let basename = path.basename(filepath); // 파일명
console.log('basename : ' + basename);
let extname = path.extname(filepath); // 확정자명
console.log('extname : ', extname);

console.log('현재 실행중인 파일 이름 : %s', __filename);
console.log('현재 실행중인 디렉토리 경로 : %s', __dirname);

console.log(path.sep); // 경로 구분자 : 윈도우는 \\, 맥과 리눅스는 /
console.log(path.delimiter); // 환경변수 구분자 : 윈도우는 ; 맥과 리눅스는 ,
console.log(path.dirname(__filename));
console.log(path.extname(__filename));
console.log(path.basename(__filename));
console.log(path.parse(__filename));
console.log(path.format({
    root: 'C:\\',
    dir:
        'C:\\Users\\happiness0110\\projects\\WebstormProjects\\node-projects\\node-study-project',
    base: 'test2.js',
    ext: '.js',
    name: 'test2'
}));
// 경로 잘못된거 고쳐줌
console.log(path.normalize("C:\\\Users\\\\happiness0110\projects\WebstormProjects/node-projects//node-study-project/test2.js"));
console.log(`이거 절대경로 맞음?: ${path.isAbsolute("/")}`);
console.log(`이거 절대경로 맞음?: ${path.isAbsolute("./")}`);
console.log(`이거 절대경로 맞음?: ${path.isAbsolute("../")}`);
console.log(`상대경로를 알려줘: ${path.relative(__filename, "c:\\users\\happiness0110")}`);
console.log(`경로를 더해줘: ${path.join(__dirname, "../")}`);
// path.resolve() : 사용법을알아보자

// 4. 파일위치 폴더위치 프로세스객체
console.log(`프로세스: ${process}`);
console.log(`프로세스 아이디: ${process.pid}`);
console.log(`프로세스 실행 위치: ${process.cwd()}`); // 프로세스 실행 위치
// process.exit();




// 10. 유틸 모듈
const util = require('util');
const dontuseme = util.deprecate((x) => {
    return x
}, '이 함수는 내일부터 지원이 중단됩니다. ');
dontuseme(1);



// 2. fs 모듈
let fs = require('fs');
fs.readdir('./test', function (err, fileList) {
    if (err) {
        console.error(err);
        return;
    }
    console.log(fileList);
});

// 이건 동기 메소드: 이렇게 하면 동기식이라서 파일 읽는데 시간을 다 쓰기떄문에 실제로는 잘 안쓴다
let data = fs.readFileSync('./read.txt', 'utf8');
console.log(data);


// 이거 다 비동기임
fs.readFile('./read.txt', 'utf8', function (err, data) {
    if (err) {
        console.error(err);
        return;
    }
    // 옵션ㅇ utf8을 주지 않으면 버퍼에 바이트로 담겨져서 data가 리턴되기 때문에 toString을 사용해야 한다
    console.log(data);
});

fs.writeFile('./write.txt', 'hello world', function (err) {
    if (err) {
        console.error(err);
        return;
    }
    console.log('파일 쓰기 성공. ');
});

fs.open('./write.txt', 'w', function (err, data) {
    if (err) {
        return console.error(err);
    }
    let buffer = new Buffer('hello world');
    fs.write(data, buffer, 0, buffer.length, null, function (err, written, buffer) {
        if (err) {
            console.log('파일 쓰면서 망함 : ' + err);
            return;
        }
        console.log('파일 다 씀');
        fs.close(data, function () {
            console.log('파일 닫았다');
        });
    });
});








// 3. 버퍼와 스트림

// 버퍼객체 알아보기
let out = 'aaaaaaa';
let buffer1 = new Buffer(10);
let len = buffer1.write(out, 'utf8');
console.log('버퍼1에 실제로 쓰인 문자열의 수 : ' + len);
console.log('버퍼1의 길이 : ' + buffer1.length);
console.log('이건 버퍼객체인가? : ' + Buffer.isBuffer(buffer1));

let byteLen = Buffer.byteLength(buffer1);
console.log(byteLen);
console.log(buffer1.toString('utf8', 0, 5));

// 스트림
const readStream = fs.createReadStream('./read.txt', {highWaterMark: 16});
const streamData = [];
readStream.on('data', (chunk) => {
    streamData.push(chunk);
    console.log('data', chunk, chunk.length);
});

readStream.on('end', () => {
    console.log('end', Buffer.concat(streamData).toString());
});

readStream.on('error', (err) => {
    console.log(err);
});

const writeStream = fs.createWriteStream('./write.txt');
writeStream.on('finish', () => {
    console.log('파일 쓰기 완료');
});

writeStream.write('hello\n');
writeStream.write('world');
writeStream.end();

// 파이프로 스트림을 연결할 수 잇다
const zlib = require('zlib');
const zlibStream = zlib.createGzip();
readStream.pipe(zlibStream).pipe(writeStream); // 압축해서 복사

// 이걸 활용한 복사 메소드
fs.copyFile('./read.txt', './write.txt', (err) => {
    console.error(err);
});




























// 웹 관련 모듈
// 4. url 모듈
// url 모듈
let url = require('url');
let parsedUrl = url.parse('http://localhost:3000/public/login1.html?id=happiness0110'); // url 문자열을 파라미터로 넘겨주면 url 객체를 리턴한다
console.log(parsedUrl.pathname);
console.log(parsedUrl.query);
console.log(url.format(parsedUrl));

console.log('params를 다 보여줘: ', parsedUrl.searchParams.getAll("key")); // 다양한 메소드가 존재함
console.log('params를 다 보여줘: ', parsedUrl.searchParams.has("key")); // 다양한 메소드가 존재함
console.log('params를 다 보여줘: ', parsedUrl.searchParams.get("key")); // 다양한 메소드가 존재함

console.log('params를 다 보여줘: ', parsedUrl.searchParams.keys()); // 다양한 메소드가 존재함
console.log('params를 다 보여줘: ', parsedUrl.searchParams.values()); // 다양한 메소드가 존재함

console.log('params를 다 보여줘: ', parsedUrl.searchParams.append("newKey", "newValue")); // 다양한 메소드가 존재함
console.log('params를 다 보여줘: ', parsedUrl.searchParams.set("key", "newValue")); // 다양한 메소드가 존재함
let finalUrl = myUrl.toString();

console.log('조작된 url: ', finalUrl);
console.log(myUrl); // url 객체
console.log(myUrl.pathname);
console.log(myUrl.query);
console.log(url.format(myUrl)); // url 객체를 파라미터로 넘겨주면 url 문자열을 리턴한다

// 5. querystring 모듈
let qs = require('querystring');
let params = qs.parse(myUrl.query);
console.log(params);
console.log(params.id);

// 방법2 : 도메인이 나와있지 않는 간략화된 주소는 아래의 방법으로 분석해야 한다
// 쿼리스트링 모듈
let parsedUrl = url.parse('https://www.youtube.com/channel/UCWhFG3MNNeD-tLlf53Xwfuw/featured');
console.log("분석된 url: ", parsedUrl);
let myQuery = qs.parse(parsedUrl.query);
console.log("분석된 url의 쿼리만 따로 분석 : ", myQuery); // 이거 안됨?
let recoveryQuery = qs.stringify(myQuery);
console.log("분석된 쿼리를 다시 원래대로: ", recoveryQuery);

console.log("재조립된 url: ", url.format(parsedUrl));

















// 9. 암호화 모듈
// 데이터를 암호화해서 전송하는 방법: 사전에 대칭키를 어떻게 공유할 것인지의 문제가 남아있다
// >> 해쉬 함수를 이용해서 데이터로부터 다이제스트 메세지를 생성
// >> 데이터 + 다이제스트 메세지를 대칭키로 암호화
// >> 전송
// >> 대칭키로 복호화해서 데이터 + 다이제스트 메세지를 얻어낸다(해커로부터 데이터 유출 방지)
// >> 해쉬함수를 이용해서 데이터로부터 다이제스트 메세지를 얻어내어 전송받은 다이제스트 메세지의 일치 여부 확인(해커의 데이터 위조 방지)
// 대칭키 방식은 des 트리플 des aes를 사용하기 때문에 속도가 빠르고 주로 웹에서 사용된다

// 데이터를 전송하고 보낸 사람을 인증하는 방법: 누구나 메세지의 내용을 들여다볼 수 있다는 문제가 남아있다
// >> 해쉬 함수를 이용해서 데이터로부터 다이제스트 메세지를 생성
// >> 다이제스트 메세지를 개인키로 암호화
// >> 데이터 + 다이제스트 메세지 전송
// >> 다이제스트 메세지를 공개키로 복호화하고 해쉬함수를 이용해서 데이터로부터 다이제스트 메세지를 얻어내어 일치 여부 확인(해커의 보낸이 위조 방지)
// >> 공개키는 인증 기관의 위계적 질서에 의해 크게 신뢰할 수 있다
// 공개키 방식은 거듭게곱 연산을 사용하기 때문에 속도가 느리고 주로 은행이나 공공기관에서 사용된다

// 웹 사용자 정보 암호화 및 인증
// 암호화: https를 사용하면 전송하는 정보를 암호화하고, 서버에서 복호화할 수 있다
// 인증: 비밀번호를 암호화하고 키와 초기벡터를 같이 전송(이 데이터들은 https로 암호화됨? 헷갈림)
let crypto = require("crypto");

// 해쉬함수로 암호화(?)
// 불안정
crypto.createHash("sha512").update("password").digest("base64");

// 안정1
crypto.randomBytes(64, (err, buf) => {
    let salt = buf.toString("base64");
    crypto.pbkdf2("password", salt, 48723, 64, "sha512", (err, key) => {
        console.log(key.toString("base64"));
    });
});

const randomBytesPromise = util.promisify(crypto.randomBytes);
const pbkdf2Promise = util.promisify(crypto.pbkdf2);

randomBytesPromise(64)
    .then((buf) => {
        const salt = buf.toString('base64');
        return pbkdf2Promise('password', salt, 48723, 64, 'sha512');
    })
    .then((key) => {
        console.log('암호화된 비밀번호: ', key.toString('base64'));
    })
    .catch((err) => {
        console.error(err);
    });

// 코드 재정리2
(async () => {
    const buf = await randomBytesPromise(64);
    const salt = buf.toString('base64');
    const key = await pbkdf2Promise('password', salt, 48723, 64, 'sha512');
    console.log('암호화된 비밀번호: ', key.toString('base64'));
})();


// 암호화
const algorithm = 'aes-192-cbc';
const keyGenerator = 'keyGenerator';
const key = crypto.scryptSync(keyGenerator, 'salt', 24);
const iv = Buffer.alloc(16, 0);

const cipher = crypto.createCipheriv(algorithm, key, iv);
let encrypted = cipher.update('hello world', 'utf8', 'hex');
encrypted += cipher.final('hex');
console.log(encrypted);

// 복호화
let decipher = crypto.createDecipheriv(algorithm, key, iv);
let plainText = decipher.update(encrypted, 'hex', 'utf8');
plainText += decipher.final();
console.log(plainText);