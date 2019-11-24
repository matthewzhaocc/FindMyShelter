/// <reference path="mesh.d.ts" />

// Card Component 
class AttributeCard extends Mesh.Component {
    render(){
        return (
            <div className="card" style="width: 18rem; display: inline-block;">
                <img className="card-img-top" src={this.attr("img")}/>
                <div className="card-body">
                    <h2>{this.attr("title")}</h2>
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