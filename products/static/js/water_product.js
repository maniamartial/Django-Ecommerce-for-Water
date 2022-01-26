 const fittingss = document.querySelector('.fit');

                        const pumps = document.querySelector('.pump');

                        const plumbings = document.querySelector('.plumb');

                        const cleanings = document.querySelector('.clean');

                        const spacecoolerss = document.querySelector('.cooler');

                        const toiletss = document.querySelector('.toilets');

                        const structuress = document.querySelector('.struct');

                        const fruitss = document.querySelector('.fruit');

                        const rains = document.querySelector('.raincoat');

                        const purifierss = document.querySelector('.purify');

                        const proofs = document.querySelector('.proof');

                        const waterpumpss = document.querySelector(".pump")

                        const floodlights = document.querySelector(".flood")

                        const fishs = document.querySelector(".aqua")

                        const ices = document.querySelector(".ice")

                        const pipess=document.querySelector(".pipes")
                        
                        
                    const filterOption = document.querySelector(".filters");
                    const all_products = document.querySelector(".all-products")
                    filterOption.addEventListener('change', filterProducts);
                   function hide(){

                            pipess.style.display="none"
                        
                        fittingss.style.display = "none";

                        pumps.style.display = "none";

                        plumbings.style.display = "none";

                        cleanings.style.display = "none";

                        spacecoolerss.style.display = "none";

                        toiletss.style.display = "none";

                        structuress.style.display = "none";

                        fruitss.style.display = "none";

                        rains.style.display = "none";

                        purifierss.style.display = "none";

                        proofs.style.display = "none";

                        waterpumpss.style.display = "none";

                        floodlights.style.display = "none";

                        fishs.style.display = "none";

                        ices.style.display = "none";

                       
                    }
                    function filterProducts(e) {
                        const product = all_products.childNodes;
                        product.forEach(function (todo) {
                            switch (e.target.value) {
                                case "fruits":
                                    console.log("Fuck u")
                                    hide();
                                         fruitss.style.display = "block";
                                    break;

                                case "coolers":
                                  hide();
                                      spacecoolerss.style.display = "block";
                                     break;

                                 case "fruits":
                                     fruitss.style.display = "none"; 
                                    console.log("fruit");
                                    break;

                                case "icecream":
                                    hide()
                                     ices.style.display = "block";
                                    break;

                                     case "floodlights":
                                         hide();
                                      floodlights.style.display = "block";
                                      break;

                                case "fish":
                                    hide();
                                     fishs.style.display = "block";
                                    break;

                                     case "structures":
                                         hide();
                                        structuress.style.display = "block";
                                    break;

                                case "pumps":
                                    hide();
                                  pumps.style.display = "block";
                                    console.log("coolers")
                                    break;

                                    case 'purifiers':
                                        hide();
                                        purifierss.style.display="block";
break;
                                     case "toilets":
                                         hide();
                                     toiletss.style.display = "block";    
                                     break;

                                case "fitting":
                                    hide();
                                      fittingss.style.display = "block";
                                    break;

                                     case "proofs":
                                         hide();
                                           proofs.style.display = "block";
                                    break;

                                case 'plumbing':
                                    hide();
                                     plumbings.style.display = "block";
                                     break;

                                case "rain":
                                    hide();
                                      rains.style.display = "block";
                                    break;

                                case 'cleaning':
                                    hide();
                                      cleanings.style.display = "block";
                                      break;

                                    case "fish":
                                        hide();
                                           fishs.style.display = "block";
                                    break;

                                case "proofs":
                                    hide();
                                     proofs.style.display = "block";
                                    break;

                                case "ice":
                                    hide();
                                        ices.style.display = "block";
                                  case "pipe":
                                      hide();
                                      pipess.style.display="block" 
                                    break;

                                    default:all_products

                            }
                        })
                    }