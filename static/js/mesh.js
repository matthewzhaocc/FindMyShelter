var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var __spreadArrays = (this && this.__spreadArrays) || function () {
    for (var s = 0, i = 0, il = arguments.length; i < il; i++) s += arguments[i].length;
    for (var r = Array(s), k = 0, i = 0; i < il; i++)
        for (var a = arguments[i], j = 0, jl = a.length; j < jl; j++, k++)
            r[k] = a[j];
    return r;
};
// Namespace w/Sub-Classes & Methods:
var Mesh;
(function (Mesh) {
    // [Node].appendChild() Wrapper:
    function render(child, parent) {
        if (parent === void 0) { parent = document.body; }
        // Convert it to Text if it's a string:
        if (typeof child == "string")
            child = document.createTextNode(child);
        parent.appendChild(child);
    }
    Mesh.render = render;
    // document.createElement() Wrapper:
    function createElement(tagName, attributes) {
        if (attributes === void 0) { attributes = {}; }
        var children = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            children[_i - 2] = arguments[_i];
        }
        // Make sure that the attributes aren't null/undefined;
        attributes = attributes || {};
        // Element to modify & return:
        var element = document.createElement(tagName);
        // Append attributes to element:
        Object.keys(attributes).forEach(function (key) {
            if (key == "className") {
                element.setAttribute("class", attributes[key]);
            }
            else {
                element.setAttribute(key, attributes[key]);
            }
        });
        // Check if children is an array:
        if (children.length && Array.isArray(children[0])) {
            children = children[0];
        }
        // Append children to element:
        children.forEach(function (child) {
            render(child, element);
        });
        // Return "furnished" element:
        return element;
    }
    Mesh.createElement = createElement;
    function ce(tagName, attributes) {
        if (attributes === void 0) { attributes = {}; }
        var children = [];
        for (var _i = 2; _i < arguments.length; _i++) {
            children[_i - 2] = arguments[_i];
        }
        return createElement.apply(void 0, __spreadArrays([tagName, attributes], children));
    }
    Mesh.ce = ce;
    // JSX Variant thru Tagged Templates (NO TypeScript):
    function tag(strings) {
        var data = [];
        for (var _i = 1; _i < arguments.length; _i++) {
            data[_i - 1] = arguments[_i];
        }
        var tagName = strings[0].replace("<", "").replace(">", "").trim();
        var attributes = data[0] || {};
        var children = data[1] || [];
        return createElement.apply(void 0, __spreadArrays([tagName, attributes], children));
    }
    Mesh.tag = tag;
    // Component Classes
    var Component = /** @class */ (function (_super) {
        __extends(Component, _super);
        function Component() {
            return _super !== null && _super.apply(this, arguments) || this;
        }
        // defo render function
        Component.prototype.render = function () { return document.createTextNode(""); };
        // get/set attr wrapper
        Component.prototype.attr = function (name, newValue) {
            if (newValue === void 0) { newValue = null; }
            if (arguments.length == 1)
                return this.getAttribute(name);
            this.setAttribute(name, newValue);
        };
        // Repaint functions
        Component.prototype.paint = function () {
            this.removeChildren();
            this.appendChild(this.render());
        };
        // Remove All Children:
        Component.prototype.removeChildren = function () {
            while (this.firstChild) {
                this.removeChild(this.firstChild);
            }
        };
        // Repaint events:
        Component.prototype.connectedCallback = function () { if (this.isConnected)
            this.paint(); };
        Component.prototype.adoptedCallback = function () { this.paint(); };
        Component.prototype.attributeChangedCallback = function () { this.paint(); };
        // customElements.define wrapper
        Component.define = function (tagName, options) {
            if (options === void 0) { options = {}; }
            customElements.define(tagName.trim(), this, options);
        };
        return Component;
    }(HTMLElement));
    Mesh.Component = Component;
    var ShadowComponent = /** @class */ (function (_super) {
        __extends(ShadowComponent, _super);
        function ShadowComponent() {
            var _this = _super !== null && _super.apply(this, arguments) || this;
            _this.shadow = _this.attachShadow({ mode: "open" });
            _this.stylesheet = {
                useStyle: false, styleText: ""
            };
            return _this;
        }
        // defo render function
        ShadowComponent.prototype.render = function () { return document.createTextNode(""); };
        // get/set attr wrapper
        ShadowComponent.prototype.attr = function (name, newValue) {
            if (newValue === void 0) { newValue = undefined; }
            if (newValue)
                return this.setAttribute(name, newValue);
            else
                return this.getAttribute(name);
        };
        // Repaint function
        ShadowComponent.prototype.paint = function () {
            this.removeChildren();
            if (this.stylesheet["useStyle"])
                this.appendChild(this.createStyle());
            this.appendChild(this.render());
        };
        // Building stylesheet for shadow-root use:
        ShadowComponent.prototype.createStyle = function () {
            var cssData = document.createElement("style");
            cssData.appendChild(document.createTextNode(this.stylesheet["styleText"]));
            return cssData;
        };
        // Override appendChild/removeChild to modify shadow-root
        ShadowComponent.prototype.appendChild = function (newChild) { return this.shadow.appendChild(newChild); };
        ShadowComponent.prototype.removeChild = function (child) { return this.shadow.removeChild(child); };
        ShadowComponent.prototype.removeChildren = function () {
            while (this.shadow.firstChild) {
                this.removeChild(this.shadow.firstChild);
            }
        };
        // Repaint events:
        ShadowComponent.prototype.connectedCallback = function () { if (this.isConnected)
            this.paint(); };
        ShadowComponent.prototype.adoptedCallback = function () { this.paint(); };
        ShadowComponent.prototype.attributeChangedCallback = function () { this.paint(); };
        // customElements.define wrapper
        ShadowComponent.define = function (tagName, options) {
            if (options === void 0) { options = {}; }
            customElements.define(tagName.trim(), this, options);
        };
        return ShadowComponent;
    }(HTMLElement));
    Mesh.ShadowComponent = ShadowComponent;
})(Mesh || (Mesh = {}));