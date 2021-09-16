package com.saccomxd.baghdadi.yassine;

import android.annotation.SuppressLint;
import android.content.Context;
import android.content.SharedPreferences;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageButton;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.bumptech.glide.Glide;
import com.chauthai.swipereveallayout.SwipeRevealLayout;
import com.chauthai.swipereveallayout.ViewBinderHelper;
import com.firebase.ui.database.FirebaseRecyclerAdapter;
import com.firebase.ui.database.FirebaseRecyclerOptions;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;
import com.squareup.picasso.Picasso;

import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class AgentAdapter extends RecyclerView.Adapter<AgentAdapter.ViewHolder> {
    private ArrayList<agent> dataModalArrayList;
    private Context context;
    private final ViewBinderHelper viewBinderHelper = new ViewBinderHelper();
    public AgentAdapter(ArrayList<agent> dataModalArrayList, Context context) {
        this.dataModalArrayList = dataModalArrayList;
        this.context = context;
    }


    @NonNull
    @Override
    public AgentAdapter.ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        return new ViewHolder(LayoutInflater.from(context).inflate(R.layout.agent, parent, false));
    }

    @Override
    public void onBindViewHolder(@NonNull AgentAdapter.ViewHolder holder, @SuppressLint("RecyclerView") int position) {

// setting data to our views in Recycler view items.
        final agent modal = dataModalArrayList.get(position);
        holder.agentName.setText(modal.getName());
        holder.agentPhone.setText(modal.getPhone());
        holder.agentGrp.setText(modal.getGrp());
//        Picasso.get().load(modal.getPic()).into(holder.agentPic);
        Glide.with(context)
                .load(modal.getPic())
                .placeholder(R.drawable.load)
                .error(R.drawable.err)
                .into(holder.agentPic);
        viewBinderHelper.setOpenOnlyOne(true);
        viewBinderHelper.bind(holder.swipRevealLayout,String.valueOf(modal.getName()));
        viewBinderHelper.closeLayout(String.valueOf(modal.getName()));
        holder.call.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
//                System.out.println();
                Toast.makeText(context, "Calling : "+modal.getPhone(), Toast.LENGTH_SHORT).show();
            }
        });

        holder.abssent.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("picktime").setValue(0);
                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("droptime").setValue(0);
                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("presence").setValue(0);
//                    Toast.makeText(itemView.getContext(), "Abssent BTN clicked", Toast.LENGTH_SHORT).show();
                holder.swipRevealLayout.close(true);

            }
        });

        holder.enter.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                @SuppressLint("SimpleDateFormat") SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
                Date date = new Date();
                String datetime = formatter.format(date);
                Toast.makeText(holder.itemView.getContext(), holder.agentName.getText() + " Entered The Van at : " + datetime.split("\\s+")[1], Toast.LENGTH_SHORT).show();
                String time = datetime.split("\\s+")[0];
                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("picktime").setValue(datetime.split("\\s+")[1]);
                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("presence").setValue("1");

                holder.swipRevealLayout.close(true);


            }
        });
        holder.leave.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                @SuppressLint("SimpleDateFormat") SimpleDateFormat formatter = new SimpleDateFormat("dd/MM/yyyy HH:mm:ss");
                Date date = new Date();
                String datetime = formatter.format(date);

                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("droptime").setValue(datetime.split("\\s+")[1]);
                holder.myRef.child(holder.user).child("trips").child(holder.currentTrip).child("agents").child(String.valueOf(position)).child("presence").setValue("1");
                Toast.makeText(holder.itemView.getContext(), "Leave BTN clicked", Toast.LENGTH_SHORT).show();
                holder.swipRevealLayout.close(true);
            }
        });

    }

    @Override
    public int getItemCount() {
        return dataModalArrayList.size();
    }

    public static class ViewHolder extends RecyclerView.ViewHolder{
        private final TextView agentName;
        private final TextView agentPhone;
        private final TextView agentGrp;
        private final ImageView agentPic;
        private final FirebaseDatabase database;
        private final DatabaseReference myRef;
        private final SharedPreferences pref;
        private final SharedPreferences.Editor editor;
        private final SwipeRevealLayout swipRevealLayout;
        private final RelativeLayout rr;
        private final ImageView enter, leave, abssent, call;
        String user, currentTrip;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            agentName = itemView.findViewById(R.id.agentName);
            agentPhone = itemView.findViewById(R.id.phone);
            agentGrp = itemView.findViewById(R.id.agrntGrp);
            agentPic = itemView.findViewById(R.id.agent_pic);

            database = FirebaseDatabase.getInstance();
            myRef = database.getReference("drivers");
            pref = itemView.getContext().getSharedPreferences("var", Context.MODE_PRIVATE);
            editor = pref.edit();
            swipRevealLayout = itemView.findViewById(R.id.swipRevealLayout);
            rr = itemView.findViewById(R.id.agentcontainer);
            currentTrip = pref.getString("trip", null);
            user = pref.getString("user", null);
            enter = itemView.findViewById(R.id.enter);
            leave = itemView.findViewById(R.id.leave);
            abssent = itemView.findViewById(R.id.absent);
            call = itemView.findViewById(R.id.call);

            rr.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if (swipRevealLayout.isOpened()){
                        swipRevealLayout.close(true);
                    }else if (swipRevealLayout.isClosed()){
                        swipRevealLayout.open(true);
                    }
                }
            });





        }
    }
}
