/// <reference path="mesh.d.ts" />
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
// Card Component 
var AttributeCard = /** @class */ (function (_super) {
    __extends(AttributeCard, _super);
    function AttributeCard() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    AttributeCard.prototype.render = function () {
        return (Mesh.ce("div", { className: "card", style: "width: 18rem; display: inline-block;" },
            Mesh.ce("img", { className: "card-img-top", src: this.attr("img") }),
            Mesh.ce("div", { className: "card-body" },
                Mesh.ce("h2", null, this.attr("title")),
                Mesh.ce("p", { className: "card-text" }, this.attr("text")),
                Mesh.ce("a", { className: "btn btn-primary", href: this.attr("href") }, this.attr("btn-text")))));
    };
    return AttributeCard;
}(Mesh.Component));
AttributeCard.define("feature-card");
