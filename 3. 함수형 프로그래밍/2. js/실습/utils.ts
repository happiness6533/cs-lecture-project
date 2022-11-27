const DIRTY_PREFIX = 'dirtyindex:';
const DIRTY_REGEX = /dirtyindex:(\d+):/;
const DIRTY_SEPARATOR_REGEX_G = /(dirtyindex:\d+:)/g;

function replaceAttribute(name: string, value: any, element: Element) {
    if (typeof value === 'function') {
        element.addEventListener(name.replace('on', '').toLowerCase(), value);
        element.removeAttribute(name);
    } else {
        console.log('This attribute is not a function');
    }
}

function buildDocumentFragmentWith(str?: string) {
    const df = document.createDocumentFragment();
    if (!str) return df;
    df.appendChild(document.createTextNode(str));

    return df;
}

function handleNoAttribute(node: Node, args: any[]) {
    if (
        node.nodeType !== Node.TEXT_NODE ||
        !node.nodeValue?.includes(DIRTY_PREFIX)
    )
        return;

    const texts = node.nodeValue.split(DIRTY_SEPARATOR_REGEX_G);

    const doms = texts.map(text => {
        const dirtyIndex = DIRTY_REGEX.exec(text)?.[1];
        if (!dirtyIndex) return buildDocumentFragmentWith(text);

        const arg = args[Number(dirtyIndex)];

        if (arg instanceof Node) {
            return arg;
        }

        return buildDocumentFragmentWith(arg);
    });

    for (const dom of doms) {
        node.parentNode?.insertBefore(dom, node);
    }
    node.nodeValue = '';
}

const jsx = (strings: TemplateStringsArray, ...args: any[]): Element => {
    if (!strings[0] && args.length) {
        throw new Error('Failed To Parse');
    }

    let template = document.createElement('div');
    template.innerHTML = strings
        .map((str, index) => {
            const argsString = args.length > index ? `${DIRTY_PREFIX}${index}:` : '';
            return `${str}${argsString}`;
        })
        .join('');

    let walker = document.createNodeIterator(template, NodeFilter.SHOW_ALL);
    let node;
    while ((node = walker.nextNode())) {
        if (
            node.nodeType === Node.TEXT_NODE &&
            node.nodeValue?.includes(DIRTY_PREFIX)
        ) {
            handleNoAttribute(node, args);
            continue;
        }

        node = <Element>node;

        let attributes: Attr[] = Array.from(node.attributes ?? []);

        for (let { name, value } of attributes) {
            console.log(name, value);
            if (name && value.includes(DIRTY_PREFIX)) {
                const match = DIRTY_REGEX.exec(value);
                if (!match) continue;
                value = args[Number(match[1])];

                replaceAttribute(name, value, node);
            }
        }
    }

    return template.firstElementChild ?? template;
};

export default jsx;