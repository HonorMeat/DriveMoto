import React, { Component } from 'react'
import classes from './Catalog.module.sass'

class Catalog extends Component{


    render() {
        return(
            <div style={{textAlign: 'center'}} className={classes.Catalog}>
                <h1>Catalog</h1>
            </div>
        )
    }
}

export default Catalog