declare namespace Mesh {
    function render(child: Node, parent?: Node): void;
    function createElement(tagName: string, attributes?: Object, ...children: any[]): HTMLElement;
    function ce(tagName: string, attributes?: Object, ...children: any[]): HTMLElement;
    class Component extends HTMLElement {
        render(): Node;
        attr(name: string, newValue?: string): string;
        paint(): void;
        removeChildren(): void;
        connectedCallback(): void;
        adoptedCallback(): void;
        attributeChangedCallback(): void;
        static define(tagName: string, options?: Object): void;
    }
    class ShadowComponent extends HTMLElement {
        shadow: ShadowRoot;
        stylesheet: Object;
        render(): Node;
        attr(name: string, newValue?: string): string | void;
        paint(): void;
        createStyle(): HTMLStyleElement;
        appendChild(newChild: any): any;
        removeChild(child: any): any;
        removeChildren(): void;
        connectedCallback(): void;
        adoptedCallback(): void;
        attributeChangedCallback(): void;
        static define(tagName: string, options?: Object): void;
    }
}