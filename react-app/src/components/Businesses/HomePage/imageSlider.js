import React, { useEffect } from 'react'
import githubicon from '../../../assets/icons/githubicon.svg'
import linkedinicon from '../../../assets/icons/linkedinicon.svg'
import websiteicon from '../../../assets/icons/websiteicon.svg'
import emailicon from '../../../assets/icons/emailicon.svg'
import './imageSlider.css'

const HomeSlider = () => {

    useEffect(() => {
        let clear1;
        let clear2;
        let clear3;
        let clear4;
        let clear5;
        let clear6;
        let clear7;
        let clear8;
        let clear9;

        function barfill1() {
            clear6 = setTimeout(() => {
                document.querySelector(".bar1").style.height = '100%';
                barfill2()
            }, 1)
        }
        function barfill2() {
            document.querySelector(".bar2").style.height = '0%';
            clear7 = setTimeout(() => {
                document.querySelector(".bar2").style.height = '100%';
                barfill3()
            }, 4500)
        }
        function barfill3() {
            document.querySelector(".bar3").style.height = '0%';
            clear8 = setTimeout(() => {
                document.querySelector(".bar3").style.height = '100%';
                barfill4()
            }, 4500)
        }
        function barfill4() {
            document.querySelector(".bar4").style.height = '0%';
            clear9 = setTimeout(() => {
                document.querySelector(".bar4").style.height = '100%';

            }, 4500)
        }
        barfill1()


        function bgFade1() {
            clear1 = setTimeout(() => {
                document.querySelector(".img1").style.opacity = 0;
                document.querySelector(".img2").style.opacity = 1;
                document.querySelector(".img3").style.opacity = 1;
                document.querySelector(".img4").style.opacity = 1;

                orderCb(["-4", "-1", "-2", "-3"], () => { bgFade2() }, 1000)
            }, 4000)
        }

        function bgFade2() {
            clear2 = setTimeout(() => {
                document.querySelector(".img1").style.opacity = 1;
                document.querySelector(".img2").style.opacity = 0;
                document.querySelector(".img3").style.opacity = 1;
                document.querySelector(".img4").style.opacity = 1;

                orderCb(["-3", "-4", "-1", "-2"], () => { bgFade3() }, 1000)
            }, 4000)
        }

        function bgFade3() {
            clear3 = setTimeout(() => {
                document.querySelector(".img1").style.opacity = 1;
                document.querySelector(".img2").style.opacity = 1;
                document.querySelector(".img3").style.opacity = 0;
                document.querySelector(".img4").style.opacity = 1;
                orderCb(["-2", "-3", "-4", "-1"], () => { bgFade4() }, 1000)
            }, 4000)
        }

        function bgFade4() {
            clear4 = setTimeout(() => {
                document.querySelector(".img1").style.opacity = 1;
                document.querySelector(".img2").style.opacity = 1;
                document.querySelector(".img3").style.opacity = 1;
                document.querySelector(".img4").style.opacity = 0;
                orderCb(["-1", "-2", "-3", "-4"], () => { bgFade1() }, 1000)
            }, 4000)
        }

        function orderCb(array, cb, time) {
            clear5 = setTimeout(() => {
                document.querySelector(".img1").style.zIndex = array[0];
                document.querySelector(".img2").style.zIndex = array[1];
                document.querySelector(".img3").style.zIndex = array[2];
                document.querySelector(".img4").style.zIndex = array[3];
                cb();
            }, time)
        }

        bgFade1();
        return () => {
            clearTimeout(clear1)
            clearTimeout(clear2)
            clearTimeout(clear3)
            clearTimeout(clear4)
            clearTimeout(clear5)
            clearTimeout(clear6)
            clearTimeout(clear7)
            clearTimeout(clear8)
            clearTimeout(clear9)
        }

    }, [])
    return (

        <div className="main-home-div">
            <div className="bar-outer-container">
                <div className="barcontainer">
                    <div className="bar1">
                    </div>
                </div>
                <div className="barcontainer">
                    <div className="bar2">
                    </div>
                </div>
                <div className="barcontainer">
                    <div className="bar3">
                    </div>
                </div>
                <div className="barcontainer">
                    <div className="bar4">
                    </div>
                </div>
            </div>
            <div className="home-img img1">
                <div className="text-contacts-container">
                    <div className="tagline">
                        In urgent need of a quick bite?
                    </div>

                </div>
            </div>

            <div className="home-img img2">

                <div className="text-contacts-container">
                    <div className="tagline">
                        Looking for the perfect date night
                    </div>

                </div>
            </div>

            <div className="home-img img3">

                <div className="text-contacts-container">
                    <div className="tagline">
                        Beer and Games?
                    </div>
                    
                </div>
            </div>

            <div className="home-img img4">

                <div className="text-contacts-container">
                    <div className="tagline">
                        Find all the restraunts you can.
                    </div>
                    
                </div>
            </div>
        </div>

    )
}

export default HomeSlider
