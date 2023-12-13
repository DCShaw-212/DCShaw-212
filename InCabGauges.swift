//
//  InCabGauges.swift
//  CDL_Pretrip_Flashcards
//
//  Created by Dustin Shaw on 1/1/23.
//

import SwiftUI

struct InCabGauges: View {
    
    private let colors: [Color] = [.gray, .white]
    private var question : String =  "Items To be Checked: \n Gauges \n Temperature//Oil Pressure//Voltmeter//Air Gauges"
    private var answer : String = "\n Check each gauge individually \n that they are functioning at a \n safe operating level."
    
    var body: some View {
        
        VStack{
            TabView{
                ForEach(colors, id: \.self) { color in
                    ZStack{
                        color.ignoresSafeArea()
                        
                        VStack{
                           
                        Text("In Cab")
                            .padding()
                            .background(.orange)
                            .font(.title2)
                            .foregroundColor(.black)
                            
                            HStack{
                                
                                Image("tempgauge").resizable()
                                    .aspectRatio(contentMode: .fit)
                                    .frame(width: 200, height: 200, alignment: .center)
                                
                                Image("oilpressure").resizable()
                                    .aspectRatio(contentMode: .fit)
                                    .frame(width: 200, height: 200, alignment: .center)
                                
                            }
                            
                            HStack{
                                
                                Image("volt").resizable()
                                    .aspectRatio(contentMode: .fit)
                                    .frame(width: 200, height: 200, alignment: .center)
                                
                                Image("airgauge").resizable()
                                    .aspectRatio(contentMode: .fit)
                                    .frame(width: 200, height: 200, alignment: .center)
                                
                            }
                           
                            
                            
                            if (color.description == "gray")
                            {
                                
                                Text("\(question)")
                                    .padding()
                                    .font(.title3)
                                    .foregroundColor(.black)
                                    .background(.white)
                                Spacer()
                            }
                            else{
                                Text("Description:")
                                    .padding()
                                    .font(.title3)
                                    .foregroundColor(.white)
                                    .background(.black)
                                Text("\(answer)")
                                    .padding()
                                    .font(.headline)
                                    .foregroundColor(.white)
                                    .background(.black)
                                Spacer()
                            }
                            
                            NavigationLink(destination:BrakeTestsLeaks()){
                                        Text("Next")
                                            .padding()
                                            .font(.title)
                                            .background(.orange)
                                            .foregroundColor(.black)
                                            .cornerRadius(60)
                                    }
                        
                            Spacer()
                        }
                    }
                    .ignoresSafeArea()
                    
                }
            }
            .tabViewStyle(.page)
            .indexViewStyle(.page(backgroundDisplayMode: .interactive))
        }
    }
}

struct InCabGauges_Previews: PreviewProvider {
    static var previews: some View {
        InCabGauges()
    }
}
