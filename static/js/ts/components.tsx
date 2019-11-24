/// <reference path="mesh.d.ts" />

// Landing Page Card Component 
class AttributeCard extends Mesh.Component {
    render(){
        return (
            <div className="card" style="text-align: center; width: 18rem; vertical-align: top; display: inline-block;">
                <img className="card-img-top" src={this.attr("img")}/>
                <div className="card-body" style="text-align: center;">
                    <h5 className="display">{this.attr("title")}</h5>
                    <p className="card-text">{this.attr("text")}</p>
                    <a className="btn btn-primary" href={this.attr("href")}>
                        {this.attr("btn-text")}
                    </a>
                </div>
            </div>
        );
    }
}
AttributeCard.define("feature-card");
